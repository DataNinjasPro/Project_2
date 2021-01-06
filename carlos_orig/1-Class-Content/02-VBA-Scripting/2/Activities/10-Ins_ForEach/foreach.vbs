Function mysum(nums As Range) as Double

    Dim elem as Variant
    Dim total as Double
    total = 0

    For Each elem in nums
        total = total + elem.value
    Next elem

    mysum = total

End Function
