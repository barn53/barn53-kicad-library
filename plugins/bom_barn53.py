# -*- coding: utf-8 -*-

"""
    @package
    Generate a HTML BOM list.
    Components are sorted by ref and grouped by value
    Fields are (if exist)
    Ref, Quantity, Value, Part, Datasheet, Description, Vendor

    Command line:
    python "pathToFile/bom_barn53.py" "%I" "%O.html"
"""

from __future__ import print_function

import kicad_netlist_reader
import sys
import os

html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <style>
        body {
          font-family: sans-serif;
          font-size: 10pt;
        }
        h1 {
          font-family: sans-serif;
        }
        </style>
    </head>
    <body>
    <h1><!--SOURCE--></h1>
    <table>
    <!--TABLEROW-->
    </table>
    <p><!--DATE--><br>
    <!--TOOL--><br>
    <!--COMPCOUNT--></p>
    </body>
</html>
    """

# Generate an instance of a generic netlist, and load the netlist tree from
# the command line option. If the file doesn't exist, execution will stop
net = kicad_netlist_reader.netlist(sys.argv[1])

# Open a file to write to, if the file cannot be opened output to stdout
# instead
try:
    f = open(sys.argv[2], 'w')
except IOError:
    e = "Can't open output file for writing: " + sys.argv[2]
    print(__file__, ":", e, file=sys.stderr)
    f = sys.stdout

components = net.getInterestingComponents()

# Output a set of rows for a header providing general information
source = os.path.split(net.getSource())
html = html.replace('<!--SOURCE-->', "BOM &ndash; " + source[-1])
html = html.replace('<!--DATE-->', net.getDate())
html = html.replace('<!--TOOL-->', net.getTool())
html = html.replace('<!--COMPCOUNT-->', "<b>Component Count:</b> " + str(len(components)))

row = '<tr style="background-color:#eee; text-align:left; line-height:20pt;"><th>Ref</th>'
row += "<th>Qnty</th>"
row += "<th>Value</th>"
row += "<th>Part</th>"
row += "<th>Footprint</th>"

html = html.replace('<!--TABLEROW-->', row + "\n<!--TABLEROW-->")

# Get all of the components in groups of matching parts + values
# (see kicad_netlist_reader.py)
grouped = net.groupComponents(components)

# Output all of the component information
color = '#000;'
count = 0
for group in grouped:
    refs = ""

    # Add the reference of every component in the group and keep a reference
    # to the component so that the other data can be filled in once per group
    for component in group:
        if len(refs) > 0:
            refs += ", "
        refs += component.getRef()
        c = component

    if count % 2 == 0:
        color = '#fff;'
    else:
        color = '#eee;'

    value = c.getValue()[0:30]
    if (len(value) > 30):
        value = value[0:30] + "…"

    # part = c.getLibName() + ":"
    part = ""
    part += c.getPartName()
    if (len(part) > 30):
        part = part[0:30] + "…"

    footprint = c.getFootprint().split(":")[-1]
    if (len(footprint) > 40):
        footprint = footprint[0:40] + "…"

    row = '<tr style="background-color:' + color + '">'
    row += '<td>' + refs
    row += '</td><td style="text-align:center;">' + str(len(group))
    row += "</td><td>" + value
    row += "</td><td>" + part
    row += "</td><td>" + footprint

    html = html.replace('<!--TABLEROW-->', row + "\n<!--TABLEROW-->")

    count += 1

# Print the formatted html to the file
print(html, file=f)
