s/^\([^-\t]*\)-\([^-\t]*\)\(\t.*$\)/\1\3\n-\3\n\2\3/g
s/^\([^-\t]*\)-\([^-\t]*\)-\([^-\t]*\)\(\t.*$\)/\1\4\n-\4\n\2\4\n-\4\n\3\4/g
s/^["”"“”]/"/g
s/^´/'/g
s/^[\–\-\–]/-/g
s/^\(R\$\)\([^\t]*\)\(\t.*\)$/\1\3\n\2\3/g
/^R\t.*$/{N; s/R\(\t[^\n]*\)\n\$[^\n]*/R$\1/ }
/^[sS][rR][aA]\t.*$/{N; s/sra\(\t[^\n]*\)\n\.[^\n]*/sra.\1/I }
/^[fF][lL][sS]\t.*$/{N; s/fls\(\t[^\n]*\)\n\.[^\n]*/fls.\1/I }
##### Temporary expressions beginning #####
s/^material\.\(\t.*\)$/material\1\n.\1/Ig
s/^social\.\(\t.*\)$/social\1\n.\1/Ig
s/^humor\.\(\t.*\)$/humor\1\n.\1/Ig
s/^também\.\(\t.*\)$/também\1\n.\1/Ig
s/^verbal\.\(\t.*\)$/verbal\1\n.\1/Ig
s/^cruz\.\(\t.*\)$/cruz\1\n.\1/Ig
s/^atual\.\(\t.*\)$/atual\1\n.\1/Ig
s/^piauí\.\(\t.*\)$/Piauí\1\n.\1/Ig
s/^mal\.\(\t.*\)$/mal\1\n.\1/Ig
s/^assim\.\(\t.*\)$/assim\1\n.\1/Ig
s/^etc\.\(\t.*\)$/etc\1\n.\1/Ig
s/^mil\.\(\t.*\)$/mil\1\n.\1/Ig
s/^anal\.\(\t.*\)$/anal\1\n.\1/Ig
s/^ar\.\(\t.*\)$/ar\1\n.\1/Ig
##### Temporary expressions end #####
s/^desta\(\t.*\)$/de\1\nesta\1/Ig
s/^noutras\(\t.*\)$/em\1\noutras\1/Ig
s/^deste\(\t.*\)$/de\1\neste\1/Ig
s/^daí\(\t.*\)$/de\1\naí\1/Ig
s/^dalém\(\t.*\)$/de\1\nalém\1/Ig
s/^do\(\t.*\)$/de\1\no\1/Ig
s/^neste\(\t.*\)$/em\1\neste\1/Ig
s/^ao\(\t.*\)$/a\1\no\1/Ig
s/^dumas\(\t.*\)$/de\1\numas\1/Ig
s/^àquelas\(\t.*\)$/a\1\naquelas\1/Ig
s/^naquilo\(\t.*\)$/em\1\naquilo\1/Ig
s/^num\(\t.*\)$/em\1\num\1/Ig
s/^daquelas\(\t.*\)$/de\1\naquelas\1/Ig
s/^duma\(\t.*\)$/de\1\numa\1/Ig
s/^daqueles\(\t.*\)$/de\1\naqueles\1/Ig
s/^nisto\(\t.*\)$/em\1\nisto\1/Ig
s/^àqueles\(\t.*\)$/a\1\naqueles\1/Ig
s/^nessas\(\t.*\)$/em\1\nestas\1/Ig
s/^naquelas\(\t.*\)$/em\1\naquelas\1/Ig
s/^doutros\(\t.*\)$/de\1\noutros\1/Ig
s/^nelas\(\t.*\)$/em\1\nelas\1/Ig
s/^naqueles\(\t.*\)$/em\1\naqueles\1/Ig
s/^neles\(\t.*\)$/em\1\neles\1/Ig
s/^dum\(\t.*\)$/de\1\num\1/Ig
s/^nas\(\t.*\)$/em\1\nas\1/Ig
s/^na\(\t.*\)$/em\1\na\1/Ig
s/^à\(\t.*\)$/a\1\na\1/Ig
s/^noutros\(\t.*\)$/em\1\noutros\1/Ig
s/^nestes\(\t.*\)$/em\1\nestes\1/Ig
s/^nisso\(\t.*\)$/em\1\nisso\1/Ig
s/^naquela\(\t.*\)$/em\1\naquela\1/Ig
s/^doutra\(\t.*\)$/de\1\noutra\1/Ig
s/^pelo\(\t.*\)$/por\1\no\1/Ig
s/^noutra\(\t.*\)$/em\1\noutra\1/Ig
s/^naquele\(\t.*\)$/em\1\naquele\1/Ig
s/^dessas\(\t.*\)$/de\1\nessas\1/Ig
s/^deles\(\t.*\)$/de\1\neles\1/Ig
s/^desses\(\t.*\)$/de\1\nesses\1/Ig
s/^delas\(\t.*\)$/de\1\nelas\1/Ig
s/^pela\(\t.*\)$/por\1\na\1/Ig
s/^noutro\(\t.*\)$/em\1\noutro\1/Ig
s/^disso\(\t.*\)$/de\1\nisso\1/Ig
s/^dela\(\t.*\)$/de\1\nela\1/Ig
s/^desse\(\t.*\)$/de\1\nesse\1/Ig
s/^nele\(\t.*\)$/em\1\nele\1/Ig
s/^dele\(\t.*\)$/de\1\nele\1/Ig
s/^dessa\(\t.*\)$/de\1\nessa\1/Ig
s/^nela\(\t.*\)$/em\1\nela\1/Ig
s/^daqui\(\t.*\)$/de\1\naqui\1/Ig
s/^às\(\t.*\)$/a\1\nas\1/Ig
s/^dali\(\t.*\)$/de\1\nali\1/Ig
s/^daquela\(\t.*\)$/de\1\naquela\1/Ig
s/^aonde\(\t.*\)$/a\1\nonde\1/Ig
s/^da\(\t.*\)$/de\1\na\1/Ig
s/^numa\(\t.*\)$/em\1\numa\1/Ig
s/^dos\(\t.*\)$/de\1\nos\1/Ig
s/^aos\(\t.*\)$/a\1\nos\1/Ig
s/^nesta\(\t.*\)$/em\1\nesta\1/Ig
s/^das\(\t.*\)$/de\1\nas\1/Ig
s/^duns\(\t.*\)$/de\1\nuns\1/Ig
s/^nesses\(\t.*\)$/em\1\nesses\1/Ig
s/^destas\(\t.*\)$/de\1\nestas\1/Ig
s/^pelas\(\t.*\)$/por\1\nas\1/Ig
s/^nos\(\t.*\)$/em\1\nos\1/Ig
s/^àquele\(\t.*\)$/a\1\naquele\1/Ig
s/^nesse\(\t.*\)$/em\1\nesse\1/Ig
s/^àquela\(\t.*\)$/a\1\naquela\1/Ig
s/^daquele\(\t.*\)$/de\1\naquele\1/Ig
s/^doutras\(\t.*\)$/de\1\noutras\1/Ig
s/^nuns\(\t.*\)$/em\1\nuns\1/Ig
s/^disto\(\t.*\)$/de\1\nisto\1/Ig
s/^no\(\t.*\)$/em\1\no\1/Ig
s/^nestas\(\t.*\)$/em\1\nestas\1/Ig
s/^destes\(\t.*\)$/de\1\nestes\1/Ig
s/^daquilo\(\t.*\)$/de\1\naquilo\1/Ig
s/^pelos\(\t.*\)$/por\1\nos\1/Ig
s/^àquilo\(\t.*\)$/a\1\naquilo\1/Ig
s/^numas\(\t.*\)$/em\1\numas\1/Ig
s/^doutro\(\t.*\)$/de\1\noutro\1/Ig
s/^nessa\(\t.*\)$/em\1\nesta\1/Ig