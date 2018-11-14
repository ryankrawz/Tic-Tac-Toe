# a1 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(a1))
# a1.grid(row=0, column=0, sticky=S+N+E+W)
#
# a2 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(a2))
# a2.grid(row=0, column=1, sticky=S+N+E+W)
#
# a3 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(a3))
# a3.grid(row=0, column=2, sticky=S+N+E+W)
#
# a4 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(a4))
# a4.grid(row=1, column=0, sticky=S+N+E+W)
#
# a5 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(a5))
# a5.grid(row=1, column=1, sticky=S+N+E+W)
#
# a6 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(a6))
# a6.grid(row=1, column=2, sticky=S+N+E+W)
#
# a7 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(a7))
# a7.grid(row=2, column=0, sticky=S+N+E+W)
#
# a8 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(a8))
# a8.grid(row=2, column=1, sticky=S+N+E+W)
#
# a9 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(a9))
# a9.grid(row=2, column=2, sticky=S+N+E+W)
#
# counter1 = 0
# counter2 = 0
#
#
# def run(b1, b2, b3, b4, b5, b6, b7, b8, b9, tally1, tally2):
#
#     if tally1 == 0:
#
#         b1 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b1))
#         b1.grid(row=0, column=0, sticky=S+N+E+W)
#
#         b2 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b2))
#         b2.grid(row=0, column=1, sticky=S+N+E+W)
#
#         b3 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b3))
#         b3.grid(row=0, column=2, sticky=S+N+E+W)
#
#         b4 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b4))
#         b4.grid(row=1, column=0, sticky=S+N+E+W)
#
#         b5 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b5))
#         b5.grid(row=1, column=1, sticky=S+N+E+W)
#
#         b6 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b6))
#         b6.grid(row=1, column=2, sticky=S+N+E+W)
#
#         b7 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b7))
#         b7.grid(row=2, column=0, sticky=S+N+E+W)
#
#         b8 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b8))
#         b8.grid(row=2, column=1, sticky=S+N+E+W)
#
#         b9 = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(b9))
#         b9.grid(row=2, column=2, sticky=S+N+E+W)
#
#         win(b1, b2, b3, b4, b5, b6, b7, b8, b9)
#         tally2 += 1
#
#     if tally1 > 0:
#
#         group = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
#         for i in group:
#             if safe(i):
#                 i = Button(area, text=' ', width=8, height=4, font='Times 30 bold', command=lambda: play(i))
#                 i.grid(row=int(group.index(i)/3), column=group.index(i)-(int(group.index(i)/3)*3), sticky=S+N+E+W)
#
#         win(b1, b2, b3, b4, b5, b6, b7, b8, b9)
#         tally2 += 1
#
#     if tally2 > tally1:
#
#         ai(b1, b2, b3, b4, b5, b6, b7, b8, b9)
#         win(b1, b2, b3, b4, b5, b6, b7, b8, b9)
#
#     tally1 += 2
#     if tally1 == 8:
#         tkMessageBox.showinfo(title='Draw', message='No one wins, it is a draw!')
#
#     return run(b1, b2, b3, b4, b5, b6, b7, b8, b9, tally1, tally2)
#
#
# run(a1, a2, a3, a4, a5, a6, a7, a8, a9, counter1, counter2)
#
#
#
# window.destroy()
