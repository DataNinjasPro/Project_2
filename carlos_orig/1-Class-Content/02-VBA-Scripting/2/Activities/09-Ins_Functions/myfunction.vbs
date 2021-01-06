'User Defined Function
Function mysum(Num1 As Double, Num2 As Double)
    mysum = Num1 + Num2
End Function

Sub call_mysum()
    MsgBox(mysum(1, 2))
End Sub
