Sub UnMerge(ws As Worksheet)
    Dim R As Range, c As Range
    Dim v As Variant
    For Each c In ws.UsedRange
        If c.MergeCells Then
            v = c.Value
            Set R = c.MergeArea
            R.UnMerge
            R.Value = v
        End If
    Next c
End Sub
A simple test to show how it is called:

Sub test()
    UnMerge Sheets(1)
End Sub