import sys

#print str(sys.argv[1])
AILPATH = str(sys.argv[1])


# -----------------------------------------------------------------------------
#
# UPDATE NAV_BAR
#
# -----------------------------------------------------------------------------

with open(AILPATH+"/var/www/templates/nav_bar.html", "r+") as f:
    a = [x.rstrip() for x in f]
    index = 0
    foundStart = False
    for item in a:
        #if item.startswith("<div class=\"collapse navbar-collapse"):
        if "collapse navbar-collapse" in item:
            foundStart = True
        elif (foundStart == True and "root.logout" in item):
            a.insert(index-1, '    </li>')
            a.insert(index-1, '    <a class="nav-link" id="page-options" href="{{ url_for(\'TwitterMon.TwitterMon_page\') }}" aria-disabled="true"><i class="fab fa-twitter"></i> Twitter Monitor</a>')
            a.insert(index-1, '    <li class="nav-item mr-3">')
            break
        index += 1
    # Go to start of file and clear it
    f.seek(0)
    f.truncate()
    # Write each line back
    for line in a:
        f.write(line + "\n")


# -----------------------------------------------------------------------------
#
# UPDATE LAUNCH.SH
#
# -----------------------------------------------------------------------------

with open(AILPATH+"/bin/LAUNCH.sh", "r+") as f:
    a = [x.rstrip() for x in f]
    index = 0
    foundStart = False
    for item in a:
        if item.startswith("function launching_scripts"):
            foundStart = True
        elif (foundStart == True and item.startswith("}")):
            a.insert(index, '    screen -S "Script_AIL" -X screen -t "TwitterAnalyzer" bash -c "cd ${AIL_BIN}; ${ENV_PY} ./TwitterAnalyzer.py; read x"')
            a.insert(index, '    sleep 0.1')
            break
        index += 1
    # Go to start of file and clear it
    f.seek(0)
    f.truncate()
    # Write each line back
    for line in a:
        f.write(line + "\n")

# -----------------------------------------------------------------------------
#
# UPDATE MODULES.CFG
#
# -----------------------------------------------------------------------------

with open(AILPATH+"/bin/packages/modules.cfg", "r+") as f:
    a = [x.rstrip() for x in f]
    index = 0
    foundStart = False
    for item in a:
        if item.startswith("[SentimentAnalysis]"):
            a.insert(index, '\n')
            a.insert(index, 'subscribe = Redis_Global')
            a.insert(index, '[TwitterAnalyzer]')
            break
        index += 1
    # Go to start of file and clear it
    f.seek(0)
    f.truncate()
    # Write each line back
    for line in a:
        f.write(line + "\n")
