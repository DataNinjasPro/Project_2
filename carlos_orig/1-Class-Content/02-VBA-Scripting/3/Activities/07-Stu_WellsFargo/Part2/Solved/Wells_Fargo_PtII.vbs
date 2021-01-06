' Steps:
' ----------------------------------------------------------------------------

' Part II:

' 1. Loop through every worksheet and select the state contents.
' 2. Copy the state contents and paste it into the Combined_Data tab

Sub WellsFargo_PtII()
    
    ' Specify the location of the combined sheet 
    Set combined_sheet = Worksheets("Combined_Data")

    ' Loop through all sheets
    For Each ws in Worksheets

        ' Find the last row of the combined sheet after each paste
        lastRow = combined_sheet.Cells(Rows.Count, "A").End(xlUp).Row + 1

        ' Copy the contents of each state sheet into the combined sheet
        combined_sheet.Range("A" & lastRow & ":G" & 30 + lastRow).Value = ws.Range("A2:G32").Value

    Next ws
End Sub


