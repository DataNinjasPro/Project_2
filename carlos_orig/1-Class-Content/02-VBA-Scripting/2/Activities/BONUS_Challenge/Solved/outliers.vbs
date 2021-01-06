' Calculates an arithmetic mean excluding outliers
Function meanmachine(nums As Range) as Double

    ' Here we define an outlier as outside of the outer fence
    ' https://www.wikihow.com/Calculate-Outliers

    ' Error checking
    if nums.Rows.Count < 3 then
        msgbox("Please enter more than three numbers")
    end if

    ' Declare variables
    Dim elem as Variant
    Dim count as Integer
    Dim sum as Double
    Dim mean as Double
    Dim q1 as Double
    Dim q3 as Double
    Dim interquartile_range as Double
    Dim outer_fence as Double
    Dim upper_boundary as Double
    Dim lower_boundary as Double

    ' Calculate Quartiles
    q1 = WorksheetFunction.QUARTILE(nums, 1)
    q3 = WorksheetFunction.QUARTILE(nums, 3)

    ' Calculate interquartile range (iqr)
    interquartile_range = q3 - q1

    ' outer_fence is 3x the iqr
    outer_fence = 3.0 * interquartile_range

    ' Calculate Boundaries
    upper_boundary = q3 + outer_fence
    lower_boundary = q1 - outer_fence

    ' Conditionally calculate the mean (average)
    count = 0
    sum = 0.0
    For Each elem in nums
        if elem.value > lower_boundary and elem.value < upper_boundary then
            sum = sum + elem.value
            count = count + 1  ' keep track of number of elements
        end if
    Next elem

    meanmachine = sum / count
End Function
