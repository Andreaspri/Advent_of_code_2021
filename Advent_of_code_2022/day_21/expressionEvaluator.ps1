### This was made to solve for x, however, it is way to complicated. Atleast it works for normal calcualtions with +-*/ and parenthesis ###


function Move-NumberToStack {
    param (
        [System.Collections.Generic.Stack[string]]$stack,
        [string]$number
    )

    if ($number[0] -eq '-') {
        if ($stack.Count -gt 0 -and $stack.Peek() -eq '-') {
            [void]$stack.Pop()
            $stack.Push('+')
            $number = $number.Replace('-', '')
            
        }
        elseif ($stack.Count -gt 0 -and $stack.Peek() -eq '+') {
            [void]$stack.Pop()

        }
    }
    elseif ($stack.Count -gt 0 -and $stack.Peek() -match '[0-9]') {
        $stack.Push('+')
    }

    for ($i = 0; $i -lt $number.Length; $i++) {
        $stack.Push($number[$i])
    }
    
}



function Get-Number {
    param (
        [System.Collections.Generic.Stack[string]]$stack
    )
    $number = ''
    while($stack.Count -gt 0 -and $stack.Peek() -match '[0-9\-\.]') {
        $temp = $stack.Pop()
        if ($stack.Count -gt 0 -and $stack.Peek() -match '[\+\-]')
        {
            $tempOperator = $stack.Pop()
            if ($stack.Count -gt 0 -and $stack.Peek() -eq 'E')
            {
                $tempE = $stack.Pop()
                $number = $tempE + $tempOperator + $temp + $number
                continue
            }
            $stack.Push($tempOperator)
        }
        $number = $temp + $number
        if ($temp -eq '-') {
            break
        }
        
    }
    return $number
}



function Invoke-Operation {
    param (
        [string]$number1,
        [string]$number2,
        [string]$operation
    )

    if ($operation -eq '+') {
        return [double]$number1 + [double]$number2
    }
    elseif ($operation -eq '-') {
        return [double]$number2 - [double]$number1
    }
    elseif ($operation -eq '*') {
        return [double]$number1 * [double]$number2
    }
    elseif ($operation -eq '/') {
        return [double]$number2 / [double]$number1
    }
    else {
        Write-Host $operation
        throw "Invalid operation $operation"
    }
}


function Invoke-MulDivLeftToRight {
    param (
        [System.Collections.Generic.Stack[string]]$stack,
        [string]$number1
    )

    while ($stack.Count -gt 0 -and $stack.Peek() -match '[\*\/]'){
        $operation = $stack.Pop()
        $number2 = Get-Number -stack $stack
        [string]$result = Invoke-Operation -number1 $number1 -number2 $number2 -operation $operation
        $number1 = $result
    }
    return $number1
}



function Invoke-CalcStack {
    param (
        [System.Collections.Generic.Stack[string]]$stack
    )
    while($true){
        # Get the first number
        $firstNumber = Get-Number -stack $stack
        if ($stack.Count -eq 0) {
            Move-NumberToStack -stack $stack -number $firstNumber
            return
        }
        if ($stack.Peek() -eq '(') {
            [void]$stack.Pop()
            $firstNumber = Invoke-MulDivLeftToRight -stack $stack -number1 $firstNumber
            Move-NumberToStack -stack $stack -number $firstNumber
            break
        }

        # Get the operation
        if ($stack.Peek() -match '[\+\-\*\/]') {
            $operation = $stack.Pop()
        }
        else {
            # This happens when we have a negative number
            $operation = '+'
        }
        
        # Get the second number
        $secondNumber = Get-Number -stack $stack
        if ($secondNumber -eq "" -and $stack.Peek() -eq '(') {
            [void]$stack.Pop()
            Move-NumberToStack -stack $stack -number $firstNumber
            break
        }
        # Invoke the operation and store it as a string
        [string]$result = Invoke-Operation -number1 $firstNumber -number2 $secondNumber -operation $operation
        # Push the result back on the stack
        Move-NumberToStack -stack $stack -number $result
    }
}


function Invoke-Equation {
    param (
        [string]$equation,
        [string]$variable
    )
    $stack = [System.Collections.Generic.Stack[string]]::new()
    $equation = $equation.Replace(' ', '')
    for ($i = 0; $i -lt $equation.Length;$i++) {
        if ($equation[$i] -eq '(') {
            $stack.Push('(')
        }
        elseif ($equation[$i] -eq ')') {
            Invoke-CalcStack -stack $stack
        }
        
        elseif ($equation[$i] -match '[0-9]' -or $equation[$i] -match "[\+\-]") {
            $stack.Push($equation[$i])
        }
        elseif ($equation[$i] -match '[\*\/]') {
            if ($equation[($i+1)] -eq '('){
                $stack.Push($equation[$i])
                continue
            }
            $number1 = Get-Number -stack $stack
            # This handles the case when we have to perform multiplication or division from left to right
            $number1 = Invoke-MulDivLeftToRight -stack $stack -number1 $number1
            $number2 = ''
            $operation = $equation[$i]
            while(($i+1) -lt $equation.Length -and $equation[($i+1)] -match '[0-9]') {
                $number2 += $equation[($i+1)]
                $i++
            }
            # Swap nubmber1 with number2
            $temp = $number1
            $number1 = $number2
            $number2 = $temp
            [string]$result = Invoke-Operation -number1 $number1 -number2 $number2 -operation $operation
            Move-NumberToStack -stack $stack -number $result
            }
        


    }
    Invoke-CalcStack -stack $stack
    return Get-Number -stack $stack
      
}