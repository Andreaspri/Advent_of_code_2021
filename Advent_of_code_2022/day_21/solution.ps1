

$data = Get-Content -Path .\data.txt



$monkeyTable = [System.Collections.Generic.Dictionary[string, string]]::new()

foreach ($line in $data) {
    $monkey, $operation = $line.Split(':')
    $operation = $operation.Replace(' ', '')
    $monkeyTable[$monkey] = $operation
}


function Get-Expression {
    param (
        [string]$monkey,
        [System.Collections.Generic.Dictionary[string, string]]$monkeyTable
    )

    if ($monkeyTable[$monkey].Contains('+')) {
        $monkey1, $monkey2 = $monkeyTable[$monkey].Split('+')
        return "($(Get-Expression -monkey $monkey1 -monkeyTable $monkeyTable ) + $(Get-Expression -monkey $monkey2 -monkeyTable $monkeyTable))"
    }
    elseif ($monkeyTable[$monkey].Contains('-')) {
        $monkey1, $monkey2 = $monkeyTable[$monkey].Split('-')
        return "($(Get-Expression -monkey $monkey1 -monkeyTable $monkeyTable ) - $(Get-Expression -monkey $monkey2 -monkeyTable $monkeyTable))"
    }
    elseif ($monkeyTable[$monkey].Contains('*')) {
        $monkey1, $monkey2 = $monkeyTable[$monkey].Split('*')
        return "($(Get-Expression -monkey $monkey1 -monkeyTable $monkeyTable ) * $(Get-Expression -monkey $monkey2 -monkeyTable $monkeyTable))"
    }
    elseif ($monkeyTable[$monkey].Contains('/')) {
        $monkey1, $monkey2 = $monkeyTable[$monkey].Split('/')
        return "($(Get-Expression -monkey $monkey1 -monkeyTable $monkeyTable ) / $(Get-Expression -monkey $monkey2 -monkeyTable $monkeyTable))"
    }
    elseif($monkeyTable[$monkey].Contains('=')) {
        $monkey1, $monkey2 = $monkeyTable[$monkey].Split('=')
        return "$(Get-Expression -monkey $monkey1 -monkeyTable $monkeyTable ) = $(Get-Expression -monkey $monkey2 -monkeyTable $monkeyTable)"
    }
    else {
        return $monkeyTable[$monkey]
    }
    
}

# Part 1. Just get the expression and evaluate it

. .\expressionEvaluator.ps1


$expression = Get-Expression -monkey 'root' -monkeyTable $monkeyTable


# Evaluate the expresion
Write-Host "Part 1:" ($expression | Invoke-Expression)


# Part 2
# Rules says that root now has = instead of whaterver he has now.
# I am the monkey humn and whatever humn is supposed to do is irrelevant.
# Replace humn will now have x and root will have = between the monkey names

$monkeyTable['humn'] = 'x'
$monkeyTable['root'] = $monkeyTable['root'].Replace('-', '=').Replace('+', '=').Replace('*', '=').Replace('/', '=')




$expression = Get-Expression -monkey 'root' -monkeyTable $monkeyTable
$left, $right = $expression.Split('=')


$currValue = 0
$mover = 0
if ($left.Contains('x'))
{
    
    $rightValue = $right | Invoke-Expression
    $currValue = $rightValue
    $mover = $rightValue
}
else {
    $rightValue = $left | Invoke-Expression
    $currValue = $rightValue
    $mover = $rightValue
    # swap right and left so that we can use the same logic
    $temp = $left
    $left = $right
    $right = $temp
}


$prevValue = $left.Replace('x', $currValue) | Invoke-Expression

while ($true)
{
    $leftValue = $left.Replace('x', $currValue) | Invoke-Expression
    if ($leftValue -eq $rightValue) {
        break
    }

    if ([Math]::Abs($leftValue - $rightValue) -gt [Math]::Abs($prevValue - $rightValue)) {
        $mover = -$mover / 2
    }

    $currValue += $mover

    $prevValue = $leftValue
        
}

Write-Host "Part 2:" $currValue





