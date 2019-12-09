#!/bin/bash

set -e

INSTALLERDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# CHECK AIL FRAMEWORK INSTALLATION AND HOME path
AIL_FRMW_PATH=~/AIL-framework/
if [[ -z "${AIL_HOME}" ]]; then
    echo "AIL Framework path (AIL_HOME) not detected"
    echo "Assuming ~/AIL-framework"
else
    AIL_FRMW_PATH=${AIL_HOME}
fi


# COPY FILES

cp ${INSTALLERDIR}/AIL_var/www/modules/TwitterMon/ ${AIL_FRMW_PATH}var/www/modules -r

cp ${INSTALLERDIR}/AIL_var/www/templates/twittermon/ ${AIL_FRMW_PATH}var/www/templates/ -r

cp ${INSTALLERDIR}/AIL_bin/TwitterAnalyzer.py ${AIL_FRMW_PATH}bin/
cp ${INSTALLERDIR}/AIL_bin/packages/Tweet.py ${AIL_FRMW_PATH}bin/packages/

# INSTALL DEPENDENCIES

${AIL_FRMW_PATH}/AILENV/bin/pip3 install pyquery
${AIL_FRMW_PATH}/AILENV/bin/pip3 install vaderSentiment

# MODIFY AIL FRAMEWORK FILES

python ${INSTALLERDIR}/modifyAIL.py $AIL_FRMW_PATH
