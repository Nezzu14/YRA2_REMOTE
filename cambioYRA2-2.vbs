If Not IsObject(application) Then
   Set SapGuiAuto  = GetObject("SAPGUI")
   Set application = SapGuiAuto.GetScriptingEngine
End If
If Not IsObject(connection) Then
   Set connection = application.Children(0)
End If
If Not IsObject(session) Then
   Set session    = connection.Children(0)
End If
If IsObject(WScript) Then
   WScript.ConnectObject session,     "on"
   WScript.ConnectObject application, "on"
End If
session.findById("wnd[0]").maximize
session.findById("wnd[0]/usr/ctxtS_CPUDT-LOW").text = "04.02.2023"
session.findById("wnd[0]/usr/ctxtS_CPUDT-LOW").setFocus
session.findById("wnd[0]/usr/ctxtS_CPUDT-LOW").caretPosition = 10
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/usr/ctxtS_CPUDT-HIGH").text = "03.03.2023"
session.findById("wnd[0]/usr/ctxtS_CPUDT-HIGH").setFocus
session.findById("wnd[0]/usr/ctxtS_CPUDT-HIGH").caretPosition = 10
session.findById("wnd[0]").sendVKey 0
session.findById("wnd[0]/tbar[1]/btn[8]").press
