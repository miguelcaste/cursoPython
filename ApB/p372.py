# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((493, 310))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_1 = wx.Button(self, wx.ID_ANY, "Descargar")
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.list_ctrl_1 = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Contador de palabras")
        self.text_ctrl_1.SetMinSize((240, 23))
        self.text_ctrl_2.SetMinSize((300, 200))
        self.list_ctrl_1.AppendColumn("Palabra", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_1.AppendColumn("Frecuencia", format=wx.LIST_FORMAT_LEFT, width=-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.WrapSizer(wx.VERTICAL)
        grid_sizer_2 = wx.FlexGridSizer(2, 2, 3, 1)
        grid_sizer_1 = wx.FlexGridSizer(1, 3, 0, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, u"Dirección:")
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER | wx.ALL | wx.FIXED_MINSIZE, 5)
        grid_sizer_1.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_1.Add(self.button_1, 0, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 2)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Texto:", style=wx.ALIGN_LEFT)
        grid_sizer_2.Add(label_2, 0, wx.TOP, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Tabla de frecuencias")
        grid_sizer_2.Add(label_3, 0, 0, 0)
        grid_sizer_2.Add(self.text_ctrl_2, 0, wx.ALL | wx.EXPAND, 2)
        grid_sizer_2.Add(self.list_ctrl_1, 1, wx.ALL | wx.EXPAND, 2)
        sizer_1.Add(grid_sizer_2, 1, wx.ALL | wx.EXPAND, 2)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()



