# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from ...Objects import (
    rgb,
    HtmlColors
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class RgbControlled:
    _prefix:str
    _sufix:str

    def __init__(self, prefix:str,sufix:str):
        self._prefix = prefix
        self._sufix = sufix

        self.Maroon                 = f"{self._prefix}{HtmlColors.Maroon                    }{self._sufix}"
        self.DarkRed                = f"{self._prefix}{HtmlColors.DarkRed                   }{self._sufix}"
        self.Brown                  = f"{self._prefix}{HtmlColors.Brown                     }{self._sufix}"
        self.Firebrick              = f"{self._prefix}{HtmlColors.Firebrick                 }{self._sufix}"
        self.Crimson                = f"{self._prefix}{HtmlColors.Crimson                   }{self._sufix}"
        self.Red                    = f"{self._prefix}{HtmlColors.Red                       }{self._sufix}"
        self.Tomato                 = f"{self._prefix}{HtmlColors.Tomato                    }{self._sufix}"
        self.Coral                  = f"{self._prefix}{HtmlColors.Coral                     }{self._sufix}"
        self.IndianRed              = f"{self._prefix}{HtmlColors.IndianRed                 }{self._sufix}"
        self.LightCoral             = f"{self._prefix}{HtmlColors.LightCoral                }{self._sufix}"
        self.DarkSalmon             = f"{self._prefix}{HtmlColors.DarkSalmon                }{self._sufix}"
        self.Salmon                 = f"{self._prefix}{HtmlColors.Salmon                    }{self._sufix}"
        self.LightSalmon            = f"{self._prefix}{HtmlColors.LightSalmon               }{self._sufix}"
        self.OrangeRed              = f"{self._prefix}{HtmlColors.OrangeRed                 }{self._sufix}"
        self.DarkOrange             = f"{self._prefix}{HtmlColors.DarkOrange                }{self._sufix}"
        self.Orange                 = f"{self._prefix}{HtmlColors.Orange                    }{self._sufix}"
        self.Gold                   = f"{self._prefix}{HtmlColors.Gold                      }{self._sufix}"
        self.DarkGoldenRod          = f"{self._prefix}{HtmlColors.DarkGoldenRod             }{self._sufix}"
        self.GoldenRod              = f"{self._prefix}{HtmlColors.GoldenRod                 }{self._sufix}"
        self.PaleGoldenRod          = f"{self._prefix}{HtmlColors.PaleGoldenRod             }{self._sufix}"
        self.DarkKhaki              = f"{self._prefix}{HtmlColors.DarkKhaki                 }{self._sufix}"
        self.Khaki                  = f"{self._prefix}{HtmlColors.Khaki                     }{self._sufix}"
        self.Olive                  = f"{self._prefix}{HtmlColors.Olive                     }{self._sufix}"
        self.Yellow                 = f"{self._prefix}{HtmlColors.Yellow                    }{self._sufix}"
        self.YellowGreen            = f"{self._prefix}{HtmlColors.YellowGreen               }{self._sufix}"
        self.DarkOliveGreen         = f"{self._prefix}{HtmlColors.DarkOliveGreen            }{self._sufix}"
        self.OliveDrab              = f"{self._prefix}{HtmlColors.OliveDrab                 }{self._sufix}"
        self.LawnGreen              = f"{self._prefix}{HtmlColors.LawnGreen                 }{self._sufix}"
        self.Chartreuse             = f"{self._prefix}{HtmlColors.Chartreuse                }{self._sufix}"
        self.GreenYellow            = f"{self._prefix}{HtmlColors.GreenYellow               }{self._sufix}"
        self.DarkGreen              = f"{self._prefix}{HtmlColors.DarkGreen                 }{self._sufix}"
        self.Green                  = f"{self._prefix}{HtmlColors.Green                     }{self._sufix}"
        self.ForestGreen            = f"{self._prefix}{HtmlColors.ForestGreen               }{self._sufix}"
        self.Lime                   = f"{self._prefix}{HtmlColors.Lime                      }{self._sufix}"
        self.LimeGreen              = f"{self._prefix}{HtmlColors.LimeGreen                 }{self._sufix}"
        self.LightGreen             = f"{self._prefix}{HtmlColors.LightGreen                }{self._sufix}"
        self.PaleGreen              = f"{self._prefix}{HtmlColors.PaleGreen                 }{self._sufix}"
        self.DarkSeaGreen           = f"{self._prefix}{HtmlColors.DarkSeaGreen              }{self._sufix}"
        self.MediumSpringGreen      = f"{self._prefix}{HtmlColors.MediumSpringGreen         }{self._sufix}"
        self.SpringGreen            = f"{self._prefix}{HtmlColors.SpringGreen               }{self._sufix}"
        self.SeaGreen               = f"{self._prefix}{HtmlColors.SeaGreen                  }{self._sufix}"
        self.MediumAquaMarine       = f"{self._prefix}{HtmlColors.MediumAquaMarine          }{self._sufix}"
        self.MediumSeaGreen         = f"{self._prefix}{HtmlColors.MediumSeaGreen            }{self._sufix}"
        self.LightSeaGreen          = f"{self._prefix}{HtmlColors.LightSeaGreen             }{self._sufix}"
        self.DarkSlateGray          = f"{self._prefix}{HtmlColors.DarkSlateGray             }{self._sufix}"
        self.Teal                   = f"{self._prefix}{HtmlColors.Teal                      }{self._sufix}"
        self.DarkCyan               = f"{self._prefix}{HtmlColors.DarkCyan                  }{self._sufix}"
        self.Aqua                   = f"{self._prefix}{HtmlColors.Aqua                      }{self._sufix}"
        self.Cyan                   = f"{self._prefix}{HtmlColors.Cyan                      }{self._sufix}"
        self.LightCyan              = f"{self._prefix}{HtmlColors.LightCyan                 }{self._sufix}"
        self.DarkTurquoise          = f"{self._prefix}{HtmlColors.DarkTurquoise             }{self._sufix}"
        self.Turquoise              = f"{self._prefix}{HtmlColors.Turquoise                 }{self._sufix}"
        self.MediumTurquoise        = f"{self._prefix}{HtmlColors.MediumTurquoise           }{self._sufix}"
        self.PaleTurquoise          = f"{self._prefix}{HtmlColors.PaleTurquoise             }{self._sufix}"
        self.AquaMarine             = f"{self._prefix}{HtmlColors.AquaMarine                }{self._sufix}"
        self.PowderBlue             = f"{self._prefix}{HtmlColors.PowderBlue                }{self._sufix}"
        self.CadetBlue              = f"{self._prefix}{HtmlColors.CadetBlue                 }{self._sufix}"
        self.SteelBlue              = f"{self._prefix}{HtmlColors.SteelBlue                 }{self._sufix}"
        self.CornFlowerBlue         = f"{self._prefix}{HtmlColors.CornFlowerBlue            }{self._sufix}"
        self.DeepSkyBlue            = f"{self._prefix}{HtmlColors.DeepSkyBlue               }{self._sufix}"
        self.DodgerBlue             = f"{self._prefix}{HtmlColors.DodgerBlue                }{self._sufix}"
        self.LightBlue              = f"{self._prefix}{HtmlColors.LightBlue                 }{self._sufix}"
        self.SkyBlue                = f"{self._prefix}{HtmlColors.SkyBlue                   }{self._sufix}"
        self.LightSkyBlue           = f"{self._prefix}{HtmlColors.LightSkyBlue              }{self._sufix}"
        self.MidnightBlue           = f"{self._prefix}{HtmlColors.MidnightBlue              }{self._sufix}"
        self.Navy                   = f"{self._prefix}{HtmlColors.Navy                      }{self._sufix}"
        self.DarkBlue               = f"{self._prefix}{HtmlColors.DarkBlue                  }{self._sufix}"
        self.MediumBlue             = f"{self._prefix}{HtmlColors.MediumBlue                }{self._sufix}"
        self.Blue                   = f"{self._prefix}{HtmlColors.Blue                      }{self._sufix}"
        self.RoyalBlue              = f"{self._prefix}{HtmlColors.RoyalBlue                 }{self._sufix}"
        self.BlueViolet             = f"{self._prefix}{HtmlColors.BlueViolet                }{self._sufix}"
        self.Indigo                 = f"{self._prefix}{HtmlColors.Indigo                    }{self._sufix}"
        self.DarkSlateBlue          = f"{self._prefix}{HtmlColors.DarkSlateBlue             }{self._sufix}"
        self.SlateBlue              = f"{self._prefix}{HtmlColors.SlateBlue                 }{self._sufix}"
        self.MediumSlateBlue        = f"{self._prefix}{HtmlColors.MediumSlateBlue           }{self._sufix}"
        self.MediumPurple           = f"{self._prefix}{HtmlColors.MediumPurple              }{self._sufix}"
        self.DarkMagenta            = f"{self._prefix}{HtmlColors.DarkMagenta               }{self._sufix}"
        self.DarkViolet             = f"{self._prefix}{HtmlColors.DarkViolet                }{self._sufix}"
        self.DarkOrchid             = f"{self._prefix}{HtmlColors.DarkOrchid                }{self._sufix}"
        self.MediumOrchid           = f"{self._prefix}{HtmlColors.MediumOrchid              }{self._sufix}"
        self.Purple                 = f"{self._prefix}{HtmlColors.Purple                    }{self._sufix}"
        self.Thistle                = f"{self._prefix}{HtmlColors.Thistle                   }{self._sufix}"
        self.Plum                   = f"{self._prefix}{HtmlColors.Plum                      }{self._sufix}"
        self.Violet                 = f"{self._prefix}{HtmlColors.Violet                    }{self._sufix}"
        self.Magenta                = f"{self._prefix}{HtmlColors.Magenta                   }{self._sufix}"
        self.Orchid                 = f"{self._prefix}{HtmlColors.Orchid                    }{self._sufix}"
        self.MediumVioletRed        = f"{self._prefix}{HtmlColors.MediumVioletRed           }{self._sufix}"
        self.PaleVioletRed          = f"{self._prefix}{HtmlColors.PaleVioletRed             }{self._sufix}"
        self.DeepPink               = f"{self._prefix}{HtmlColors.DeepPink                  }{self._sufix}"
        self.HotPink                = f"{self._prefix}{HtmlColors.HotPink                   }{self._sufix}"
        self.LightPink              = f"{self._prefix}{HtmlColors.LightPink                 }{self._sufix}"
        self.Pink                   = f"{self._prefix}{HtmlColors.Pink                      }{self._sufix}"
        self.AntiqueWhite           = f"{self._prefix}{HtmlColors.AntiqueWhite              }{self._sufix}"
        self.Beige                  = f"{self._prefix}{HtmlColors.Beige                     }{self._sufix}"
        self.Bisque                 = f"{self._prefix}{HtmlColors.Bisque                    }{self._sufix}"
        self.BlanchedAlmond	        = f"{self._prefix}{HtmlColors.BlanchedAlmond	        }{self._sufix}"
        self.Wheat                  = f"{self._prefix}{HtmlColors.Wheat                     }{self._sufix}"
        self.CornSilk               = f"{self._prefix}{HtmlColors.CornSilk                  }{self._sufix}"
        self.LemonChiffon           = f"{self._prefix}{HtmlColors.LemonChiffon              }{self._sufix}"
        self.LightGoldenRodYellow   = f"{self._prefix}{HtmlColors.LightGoldenRodYellow      }{self._sufix}"
        self.LightYellow            = f"{self._prefix}{HtmlColors.LightYellow               }{self._sufix}"
        self.SaddleBrown            = f"{self._prefix}{HtmlColors.SaddleBrown               }{self._sufix}"
        self.Sienna                 = f"{self._prefix}{HtmlColors.Sienna                    }{self._sufix}"
        self.Chocolate              = f"{self._prefix}{HtmlColors.Chocolate                 }{self._sufix}"
        self.Peru                   = f"{self._prefix}{HtmlColors.Peru                      }{self._sufix}"
        self.SandyBrown             = f"{self._prefix}{HtmlColors.SandyBrown                }{self._sufix}"
        self.BurlyWood              = f"{self._prefix}{HtmlColors.BurlyWood                 }{self._sufix}"
        self.Tan                    = f"{self._prefix}{HtmlColors.Tan                       }{self._sufix}"
        self.RosyBrown              = f"{self._prefix}{HtmlColors.RosyBrown                 }{self._sufix}"
        self.Moccasin               = f"{self._prefix}{HtmlColors.Moccasin                  }{self._sufix}"
        self.NavajoWhite            = f"{self._prefix}{HtmlColors.NavajoWhite               }{self._sufix}"
        self.PeachPuff              = f"{self._prefix}{HtmlColors.PeachPuff                 }{self._sufix}"
        self.MistyRose              = f"{self._prefix}{HtmlColors.MistyRose                 }{self._sufix}"
        self.LavenderBlush          = f"{self._prefix}{HtmlColors.LavenderBlush             }{self._sufix}"
        self.Linen                  = f"{self._prefix}{HtmlColors.Linen                     }{self._sufix}"
        self.OldLace                = f"{self._prefix}{HtmlColors.OldLace                   }{self._sufix}"
        self.PapayaWhip             = f"{self._prefix}{HtmlColors.PapayaWhip                }{self._sufix}"
        self.WeaShell               = f"{self._prefix}{HtmlColors.WeaShell                  }{self._sufix}"
        self.MintCream              = f"{self._prefix}{HtmlColors.MintCream                 }{self._sufix}"
        self.SlateGray              = f"{self._prefix}{HtmlColors.SlateGray                 }{self._sufix}"
        self.LightSlateGray         = f"{self._prefix}{HtmlColors.LightSlateGray            }{self._sufix}"
        self.LightSteelBlue         = f"{self._prefix}{HtmlColors.LightSteelBlue            }{self._sufix}"
        self.Lavender               = f"{self._prefix}{HtmlColors.Lavender                  }{self._sufix}"
        self.FloralWhite            = f"{self._prefix}{HtmlColors.FloralWhite               }{self._sufix}"
        self.AliceBlue              = f"{self._prefix}{HtmlColors.AliceBlue                 }{self._sufix}"
        self.GhostWhite             = f"{self._prefix}{HtmlColors.GhostWhite                }{self._sufix}"
        self.Honeydew               = f"{self._prefix}{HtmlColors.Honeydew                  }{self._sufix}"
        self.Ivory                  = f"{self._prefix}{HtmlColors.Ivory                     }{self._sufix}"
        self.Azure                  = f"{self._prefix}{HtmlColors.Azure                     }{self._sufix}"
        self.Snow                   = f"{self._prefix}{HtmlColors.Snow                      }{self._sufix}"
        self.Black                  = f"{self._prefix}{HtmlColors.Black                     }{self._sufix}"
        self.DimGray                = f"{self._prefix}{HtmlColors.DimGray                   }{self._sufix}"
        self.Gray	                = f"{self._prefix}{HtmlColors.Gray	                    }{self._sufix}"
        self.DarkGray	            = f"{self._prefix}{HtmlColors.DarkGray	                }{self._sufix}"
        self.Silver	                = f"{self._prefix}{HtmlColors.Silver	                }{self._sufix}"
        self.LightGray	            = f"{self._prefix}{HtmlColors.LightGray	                }{self._sufix}"
        self.Gainsboro              = f"{self._prefix}{HtmlColors.Gainsboro                 }{self._sufix}"
        self.WhiteSmoke             = f"{self._prefix}{HtmlColors.WhiteSmoke                }{self._sufix}"
        self.White                  = f"{self._prefix}{HtmlColors.White                     }{self._sufix}"

    def custom(self, color:rgb):
      return f"{self._prefix}{color}{self._sufix}"

    def c(self,color:rgb): #synonim for cls.custom()
      return self.custom(color)

    def rgb(self, r:int,g:int,b:int):
      return f"{self._prefix}{rgb(r,g,b)}{self._sufix}"