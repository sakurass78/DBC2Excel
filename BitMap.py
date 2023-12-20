
#Msg结构
#columns=["Message Name", "CAN ID", "Cyclic Time", "Msg Len", "Signal", "Description",
#                                            "StartBit", "Length", "Factor", "Offset", "Unit",
#                                            "Minimum Physical", "Maximum Physical", "Update_Factor",
#                                             "Update_Offset", "Update_Minimum", "Update_Maximum",
#                                            "Init Value"]

#Color RGB
Yellow = "FFFFCC"
Red = "FF0000"
Blue = "0000FF"
Green = "00FF00"
Pink = "FFC0CB"
Purple = "A020F0"
Brown = "A52A2A"
Orange = "FFA500"
LimeGreen = "32CD32"
Chocolate4 = "8B4513"
Goldenrod4 = "8B6914"
PeachPuff = "FFDAB9"

Color = [Red,Blue,Brown,Purple,Green,Orange,Pink,LimeGreen,Chocolate4,PeachPuff]

class BitMap():

    # 初始化整个Class
    def __init__(self, Msg):

        # 创建 BitMap计算类
        self.Msg = Msg


    def BitMapping(self):
        #初始化 bit 位图
        BitList = [[7, 6, 5, 4, 3, 2, 1, 0,
                   15,14,13,12,11,10, 9, 8,
                   23,22,21,20,19,18,17,16,
                   31,30,29,28,27,26,25,24,
                   39,38,37,36,35,34,33,32,
                   47,46,45,44,43,42,41,40,
                   55,54,53,52,51,50,49,48,
                   63,62,61,60,59,58,57,56],
                   [Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow,
                    Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow,
                    Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow,
                    Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow,
                    Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow,
                    Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow,
                    Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow,
                    Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow, Yellow]]

        #num为该报文的信号个数
        num = self.Msg.index

        for i in num:
            if self.Msg.loc[i, "StartBit"] > 63 or self.Msg.loc[i, "StartBit"] + self.Msg.loc[i, "Length"] > 63:
                break
            else:
                BitList = self.BitCal(BitList, self.Msg.loc[i, "Signal"], self.Msg.loc[i, "StartBit"], self.Msg.loc[i, "Length"], i % 10)

        return BitList

    def BitCal(self,BitList, MsgName, StartBit, Length, num):
        for i in range(0, 64):
            if BitList[0][i] == StartBit:
                BitList[0][i] = MsgName
                break
        for j in range(0, Length):
            BitList[1][i + j] = Color[num]
        return BitList

