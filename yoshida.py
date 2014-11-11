#coding:utf-8

class coin(object):
    def __init__(self,val):
        self.val = val
    def C500(self,c500):
        a = self.val / 500  #余りは消去
        if c500 >= a:
            return self.val - 500 * a #余りは消去してあるのでよい？
        else:
            return self.val - 500 * c500
    def C100(self,c100):
        a = self.val.C500() / 100
        if c100 >= a:
            return self.val.C500() - 100 * a
        else:
            return self.val.C500() - 100 * c100
    def C50(self,c50):
        a = self.val.C500().C100() /50
        if c50 >= a:
            return self.val.C500().C100() - 50 * a
        else:
            return self.val.C500.C100() - 50 * c50
    def C10(self,c10):
        a = self.val.C500().C100().C50() /10
        if c10 >= a:
            return self.val.C500().C100().C50() - 10 * a
        else:
            return self.val.C500.C100().C50() - 10 * c10
    def C5(self,c5):
        a = self.val.C500().C100().C50().C10() / 5
        if c5 >= a:
            return self.val.C500().C100().C50().C10() - 5 * a
        else:
            return self.val.C500.C100().C50().C10() - 5 * c5
    def C1(self,c1):
        a = self.val.C500().C100().C50().C10().C5() / 1
        if c1 >= a:
            return self.val.C500().C100().C50().C10().C5() - 1 * a
        else:
            return self.val.C500.C100().C50().C10().C5() - 1 * c5

# def C500(c500,A):
#     a = A / 500
#     if c500 >= a:
#         return a
#     else:
#         return c500
#
# def C100(c100,B):
#     b = B / 100
#     if c100 >= b:
#         return b
#     else:
#         return c100
#
# def C50(c50,C):
#     c = C / 50
#     if c50 >= c:
#         return c
#     else:
#         return c50
#
# def C10(c10,D):
#     d = D / 10
#     if c10 >= d:
#         return d
#     else:
#         return c10
#
# def C5(c5,E):
#     e = E / 5
#     if c5 >= e:
#         return e
#     else:
#         return c5
#
# def C1(c1,F):
#     f = F / 1
#     if c1 >= f:
#         return f
#     else:
#         return c1
#
#
# def coin(c1,c5,c10,c50,c100,c500,A):
#     a = C500(c500,A)
#     B = A-500*a
#     b = C100(c100,B)
#     C = B-100*b
#     c = C50(c50,C)
#     D = C-50*c
#     d = C10(c10,D)
#     E = D-10*d
#     e = C5(c5,E)
#     F = E-5*e
#     f = C1(c1,F)
#     return a+b+c+d+e+f
#
#
# print coin(3,2,1,3,0,2,620)

print coin(620).C500(2)