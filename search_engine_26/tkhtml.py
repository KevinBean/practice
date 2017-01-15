# -*- coding=utf-8 -*-
import urllib

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from tkinterhtml import HtmlFrame

root = tk.Tk()

frame = HtmlFrame(root, horizontal_scrollbar="auto")
frame.grid(sticky=tk.NSEW)

frame.set_content("""
<html>

<head>
<meta name=标题 content="">
<meta name=关键词 content="">
<meta http-equiv=Content-Type content="text/html; charset=x-mac-chinesesimp">
<meta name=Generator content="Microsoft Word 14 (filtered)">
<style>
<!--
 /* Font Definitions */
@font-face
	{font-family:宋体;
	panose-1:2 1 6 0 3 1 1 1 1 1;}
@font-face
	{font-family:宋体;
	panose-1:2 1 6 0 3 1 1 1 1 1;}
@font-face
	{font-family:"\@宋体";
	panose-1:2 1 6 0 3 1 1 1 1 1;}
 /* Style Definitions */
p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin:0cm;
	margin-bottom:.0001pt;
	text-align:justify;
	text-justify:inter-ideograph;
	font-size:10.5pt;
	font-family:"Times New Roman";}
 /* Page Definitions */
@page WordSection1
	{size:595.3pt 841.9pt;
	margin:72.0pt 90.0pt 72.0pt 90.0pt;
	layout-grid:15.6pt;}
div.WordSection1
	{page:WordSection1;}
-->
</style>

</head>

<body lang=ZH-CN style='text-justify-trim:punctuation'>

<div class=WordSection1 style='layout-grid:15.6pt'>

<p class=MsoNormal><span style='font-size:9.0pt;font-family:宋体'>（格式编号<span
lang=EN-US>202025</span>－<span lang=EN-US>R1</span>－<span lang=EN-US>2008</span>）</span></p>

<p class=MsoNormal align=center style='text-align:center'><span
style='font-family:宋体'>北</span> <span style='font-family:宋体'>京</span> <span
style='font-family:宋体;letter-spacing:-.8pt'>电<span lang=EN-US>&nbsp; </span>力<span
lang=EN-US>&nbsp; </span></span><span style='font-family:宋体'>设</span> <span
style='font-family:宋体'>计</span> <span style='font-family:宋体'>院</span></p>

<p class=MsoNormal align=center style='text-align:center'><b><span
style='font-size:18.0pt;font-family:宋体'>质</span></b><b><span style='font-size:
18.0pt'> </span></b><b><span style='font-size:18.0pt;font-family:宋体'>量</span></b><b><span
style='font-size:18.0pt'> </span></b><b><span style='font-size:18.0pt;
font-family:宋体'>信</span></b><b><span style='font-size:18.0pt'> </span></b><b><span
style='font-size:18.0pt;font-family:宋体'>息</span></b><b><span style='font-size:
18.0pt'> </span></b><b><span style='font-size:18.0pt;font-family:宋体'>反</span></b><b><span
style='font-size:18.0pt'> </span></b><b><span style='font-size:18.0pt;
font-family:宋体'>馈</span></b><b><span style='font-size:18.0pt'> </span></b><b><span
style='font-size:18.0pt;font-family:宋体'>单</span></b></p>

<p class=MsoNormal><span lang=EN-US>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style='font-family:宋体'>编</span>
<span style='font-family:宋体'>号：</span><span lang=EN-US>10</span><span
style='font-family:宋体'>－</span><span lang=EN-US>2011</span><span
style='font-family:宋体'>－</span><span lang=EN-US>01</span></p>

<table class=MsoNormalTable border=1 cellspacing=0 cellpadding=0 width=486
 style='margin-left:-34.6pt;border-collapse:collapse;border:none'>
 <tr style='height:22.0pt'>
  <td width=99 valign=top style='width:99.0pt;border-top:1.5pt;border-left:
  1.5pt;border-bottom:1.0pt;border-right:1.0pt;border-color:black;border-style:
  solid;padding:0cm 1.4pt 0cm 1.4pt;height:22.0pt'>
  <p class=MsoNormal style='text-indent:21.0pt;line-height:20.0pt'><span
  style='font-family:宋体'>信息名称</span></p>
  </td>
  <td width=165 valign=top style='width:165.0pt;border-top:solid black 1.5pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 1.4pt 0cm 1.4pt;height:22.0pt'>
  <p class=MsoNormal align=center style='text-align:center;line-height:20.0pt'><span
  style='font-family:宋体'>变电站主变增容工程应充分考虑施工临时过渡过程</span></p>
  </td>
  <td width=78 valign=top style='width:78.0pt;border-top:solid black 1.5pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 1.4pt 0cm 1.4pt;height:22.0pt'>
  <p class=MsoNormal align=center style='text-align:center;line-height:20.0pt'><span
  style='font-family:宋体'>填卡人员</span></p>
  </td>
  <td width=144 valign=top style='width:144.0pt;border-top:solid black 1.5pt;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.5pt;
  padding:0cm 1.4pt 0cm 1.4pt;height:22.0pt'>
  <p class=MsoNormal align=center style='text-align:center;line-height:20.0pt'><span
  style='font-family:宋体'>李雪男</span></p>
  </td>
 </tr>
 <tr style='height:22.0pt'>
  <td width=99 valign=top style='width:99.0pt;border-top:none;border-left:solid black 1.5pt;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0cm 1.4pt 0cm 1.4pt;
  height:22.0pt'>
  <p class=MsoNormal style='text-indent:21.0pt;line-height:20.0pt'><span
  style='font-family:宋体'>信息来源</span></p>
  </td>
  <td width=165 valign=top style='width:165.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 1.4pt 0cm 1.4pt;height:22.0pt'>
  <p class=MsoNormal align=center style='text-align:center;line-height:20.0pt'><span
  style='font-family:宋体'>回龙观<span lang=EN-US>220kV</span>站主变增容改造工程</span></p>
  </td>
  <td width=78 valign=top style='width:78.0pt;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;padding:0cm 1.4pt 0cm 1.4pt;
  height:22.0pt'>
  <p class=MsoNormal align=center style='text-align:center;line-height:20.0pt'><span
  style='font-family:宋体'>填卡日期</span></p>
  </td>
  <td width=144 valign=top style='width:144.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.5pt;
  padding:0cm 1.4pt 0cm 1.4pt;height:22.0pt'>
  <p class=MsoNormal align=center style='text-align:center;line-height:20.0pt'><span
  lang=EN-US>2011-2-28</span></p>
  </td>
 </tr>
 <tr style='height:22.0pt'>
  <td width=486 colspan=4 valign=top style='width:486.0pt;border-top:none;
  border-left:solid black 1.5pt;border-bottom:solid black 1.0pt;border-right:
  solid black 1.5pt;padding:0cm 1.4pt 0cm 1.4pt;height:22.0pt'>
  <p class=MsoNormal style='text-indent:21.75pt;line-height:20.0pt'><span
  style='font-family:宋体'>信息内容：</span></p>
  <p class=MsoNormal style='text-indent:21.75pt;line-height:20.0pt'><span
  style='font-family:宋体'>在回龙观</span><span lang=EN-US>220kV</span><span
  style='font-family:宋体'>站主变增容改造工程中，由于回龙观站主变重载，在</span><span lang=EN-US>2011</span><span
  style='font-family:宋体'>年度夏前要将</span><span lang=EN-US>2</span><span
  style='font-family:宋体'>台</span><span lang=EN-US>180MVA</span><span
  style='font-family:宋体'>的主变增容至</span><span lang=EN-US>2</span><span
  style='font-family:宋体'>台</span><span lang=EN-US>250MVA</span><span
  style='font-family:宋体'>主变。</span></p>
  <p class=MsoNormal style='text-indent:21.75pt;line-height:20.0pt'><span
  style='font-family:宋体'>由于工程的特殊性，及与设总、相关部门沟通不足：昌平区经济发展较快，其负荷增长水平高于北京市平均水平，且回龙观站现状处于满载状态，在施工过渡期间有</span><span
  lang=EN-US>1</span><span style='font-family:宋体'>台</span><span lang=EN-US>180MVA</span><span
  style='font-family:宋体'>的主变将带全站负荷，如果不考虑负荷的转移将导致施工期间单台主变过载运行，在可研审核会中会议没有明确要增加施工过渡期间的负荷分析及临时切改方案，会后设计人没有与设总、相关部门在这个问题上进行沟通，导致可研报告缺少施工过渡期间负荷分析及临时切改方案论述的内容。</span></p>
  <p class=MsoNormal style='text-indent:21.75pt;line-height:20.0pt'><span
  lang=EN-US>&nbsp;</span></p>
  </td>
 </tr>
 <tr style='height:22.0pt'>
  <td width=486 colspan=4 valign=top style='width:486.0pt;border-top:none;
  border-left:solid black 1.5pt;border-bottom:solid black 1.0pt;border-right:
  solid black 1.5pt;padding:0cm 1.4pt 0cm 1.4pt;height:22.0pt'>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;&nbsp;&nbsp;
  </span><span style='font-family:宋体'>信息分析及处理意见：</span></p>
  <p class=MsoNormal style='text-indent:21.0pt;line-height:20.0pt'><span
  style='font-family:宋体'>出现以上问题的原因主要是：做工程之前要对工程的特殊性有充分的了解，审核会中要把有疑问的地方要求在会议上明确，要做到主动与设总、相关部门及时沟通。</span></p>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;</span></p>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;</span></p>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;</span></p>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span
  style='font-family:宋体'>室主任：</span> <span lang=EN-US>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2011
  </span><span style='font-family:宋体'>年</span><span lang=EN-US>&nbsp; 2</span><span
  style='font-family:宋体'>月</span> <span lang=EN-US>28 </span><span
  style='font-family:宋体'>日</span></p>
  </td>
 </tr>
 <tr style='height:22.0pt'>
  <td width=486 colspan=4 valign=top style='width:486.0pt;border:solid black 1.5pt;
  border-top:none;padding:0cm 1.4pt 0cm 1.4pt;height:22.0pt'>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;&nbsp;&nbsp;
  </span><span style='font-family:宋体'>处理结果：</span></p>
  <p class=MsoNormal align=center style='text-align:center;line-height:20.0pt'><span
  lang=EN-US>&nbsp;</span></p>
  <p class=MsoNormal style='text-indent:21.0pt;line-height:20.0pt'><span
  style='font-family:宋体'>回龙观</span><span lang=EN-US>220kV</span><span
  style='font-family:宋体'>站主变增容改造工程中增加过渡方案的说明。</span></p>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;</span></p>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;</span></p>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;</span></p>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;</span></p>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;</span></p>
  <p class=MsoNormal style='line-height:20.0pt'><span lang=EN-US>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></p>
  <p class=MsoNormal style='text-indent:105.0pt;line-height:20.0pt'><span
  lang=EN-US>&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span
  style='font-family:宋体'>责任部门主管：</span><span lang=EN-US>&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span
  style='font-family:宋体'>年</span><span lang=EN-US>&nbsp;&nbsp;&nbsp; &nbsp;</span><span
  style='font-family:宋体'>月</span> &nbsp;<span lang=EN-US>&nbsp;&nbsp;</span><span
  style='font-family:宋体'>日</span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>

</div>

</body>

</html>

""")

# frame.set_content(urllib.urlopen("http://www.baidu.com").read().decode())
# print(frame.html.cget("zoom"))


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()