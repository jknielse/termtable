import termtable

cols = ['Name', 'Position', 'Thingy']
rows = [
    ['Joe', 'CEO', 'A thing'],
    ['Fred', 'CFO', 'Another thing'],
    ['Bob', 'CTO', 'One more thing'],
    ['Bloop', 'Court Jester', 'Additional thing'],
]

tt = termtable.TerminalTable(cols, rows)

print 'Showing table:\n'
tt.show()

print 'Single selection from table:\n'
index = tt.prompt_selection('Please select a row:')
selection = rows[index]
print 'Selected:'
print selection
print ''

print 'Multi selection from table:\n'
selections = [rows[r] for r in tt.prompt_selection('Please select some rows:', multi_select=True)]
print 'Selected:'
for s in selections:
  print s
print ''

print 'Dangerous selection from table:\n'
selections = [rows[r] for r in tt.prompt_selection('Please select a row... but be careful!', multi_select=True, danger=True)]
print 'Selected:'
for s in selections:
  print s
print ''

print 'Sub-editing from table:\n'

subcols = ['Position']
subrows = [
    ['CEO'],
    ['CFO'],
    ['CTO'],
    ['Court Jester'],
    ['Something much longer! wow such long much amaze']
]

subtable = termtable.TerminalTable(subcols, subrows, header=False)

def controller(key, index):
    global subtable
    if key == 'q':
        return 'ABANDON', []
    if key == ' ':
        sub_selection = subtable.prompt_selection(startx=tt.column_position(1) - 1, starty=tt.row_position(index) - 1)
        if sub_selection is not None:
            newrow = [rows[index][0], subrows[sub_selection][0], rows[index][2]]
            return 'REPLACE', [newrow]
        else:
            return 'REDRAW', []
    if key == 'BACKSPACE':
        return 'REMOVE', [index]
    if key == '+':
        return 'INSERT', [0, ['Secret Bob', 'Magician', 'Of the high realm']]
    if key == 'ENTER':
        return 'COMMIT', []

tt.interact(controller)
