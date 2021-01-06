Function mymean(nums As Range) as Double

    Dim elem as Variant
    Dim sum as Double
    Dim count as Double
    sum = 0
    count = 0

    For Each elem in nums
        sum = sum + elem.value
        count = count + 1
    Next elem

    ' We could also have gotten the count this way
    ' count = nums.Rows.Count
    mymean = sum / count

End Function
