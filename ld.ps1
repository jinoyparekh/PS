#input param
$foo = @('a','b','c','d','e','d','c','b','a')

#Finds the first recurring char from input
function checker($foo)
{
    $baz = New-Object System.Collections.Generic.List[System.Object] 
    ForEach($bar in $foo)
    {
        if ($baz.Contains($bar))
        {
            return $bar
        }
        else
        {
            $baz.Add($bar) 
        }
    }
}
