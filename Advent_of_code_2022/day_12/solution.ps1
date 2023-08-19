
# Find the shortest path from start to goal.
# Rules:
# 1. You can only move up one letter (i.e., a->b c->d) S == a and E == z
# 2. You have no fall damage. Jump from x to a if you want
# 3. You can only move manhattan style (i.e., not diagonally)



# Implementing a bfs to solve it

function Find-ShortestPath {
    param (
        [Parameter(Mandatory=$true)][string]$goal,
        [Parameter(Mandatory=$true)][array]$data,
        [Parameter(Mandatory=$true)][array]$startPos

    )
    $startPos += 0
    $visited = [System.Collections.Hashtable]::new()
    $waveFront = [System.Collections.Queue]::new()
    $waveFront.Enqueue($startPos)
    $visited.Add("($($startPos[0]),$($startPos[1]))",0)
    while ($waveFront.Count -gt 0) {
        $x, $y, $depth = $waveFront.Dequeue()
        $currentChar = $data[$x][$y]
        
        if ($currentChar -ceq "S")
        {
            $currentChar = "a"
        }

        $moves = @(
        @(($x-1),$y), # North
        @(($x+1),$y), # South
        @($x,($y-1)), # West
        @($x,($y+1))  # East
        )
        foreach ($move in $moves) {
            $x, $y = $move
            if ($x -ge 0 -and $x -lt $data.Count -and $y -ge 0 -and $y -lt $data[$x].Length) {
                if ($data[$x][$y] -ceq $goal){
                    $destinationChar = "z"
                }
                else {
                    $destinationChar = $data[$x][$y]
                }
                if (([byte][char]$currentChar - [byte][char]$destinationChar) -gt -2){
                    if (!$visited.ContainsKey("($x,$y)")) {
                        if ($goal -ceq $data[$x][$y])
                        {
                            return $depth+1
                        }
                        $waveFront.Enqueue(@($x,$y,($depth+1)))
                        $visited.Add("($x,$y)",$depth+1)
                    }
                }
            }
        }
    }
}




function Start-Part1 {


    # Read file
    $data = Get-Content .\data.txt

    $goal = "E"

    # Find start position
    for ($i = 0; $i -lt $data.Count; $i++)
    {
        for ($j = 0; $j -lt $data[$i].Length; $j++) {
            if ($data[$i][$j] -ceq "S")
            {
                $startPos = $i, $j
                break
            }
        }
    }

    # Find shortest path
    $shortestPath = Find-ShortestPath -goal $goal -data $data -startPos $startPos

    Write-Host "Shortest path from S to E is $($shortestPath) steps long"
    return $shortestPath
}


function Start-Part2 {
    param(
        [Parameter(ValueFromPipeline=$true)]
        [int]$shortestPath
    )

    # Read file
    $data = Get-Content .\data.txt

    $goal = "E"
    $startPositions = [System.Collections.ArrayList]::new()

    for ($i = 0; $i -lt $data.Count; $i++)
    {
        for ($j = 0; $j -lt $data[$i].Length; $j++) {
            if ($data[$i][$j] -ceq "a" -or $data[$i][$j] -ceq "S")
            {
                [void]$startPositions.Add(@($i, $j))

            }
        }
    }

    foreach ($startPos in $startPositions) {
        $newPath = Find-ShortestPath -goal $goal -data $data -startPos $startPos
        if ($newpath -and $newPath -lt $shortestPath) {
            $shortestPath = $newPath
        }
    }

    Write-Host "The shortest possible path from any a or S to E is $($shortestPath) steps long"


}


Start-Part1 | Start-Part2