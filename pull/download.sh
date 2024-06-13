        sudo apt update
        sudo apt -y install xmltv retry
        go install github.com/aquilax/m3u-combine@latest
        cd /home/runner/work/newf276/junk/pull
        wget -O ptv-us.m3u https://i.mjh.nz/PlutoTV/us.m3u8
        wget -O ptv-ca.m3u https://i.mjh.nz/PlutoTV/ca.m3u8
        wget -O ptv-gb.m3u https://i.mjh.nz/PlutoTV/gb.m3u8
        wget -O roku.m3u https://i.mjh.nz/Roku/all.m3u8
        curl -H "Authorization: token $JAPAN" \
        -H 'Accept: application/vnd.github.v3.raw' \
        -o playlist.m3u \
        -L $JP3
        curl -H "Authorization: token $JAPAN" \
        -H 'Accept: application/vnd.github.v3.raw' \
        -o playlist.m3u \
        -L $TWO
        wget -O pluto.xml https://i.mjh.nz/PlutoTV/all.xml
        wget -O roku.xml https://i.mjh.nz/Roku/epg.xml
        wget -O epg_ripper_CA1.xml https://epgshare01.online/epgshare01/epg_ripper_CA1.xml.gz
        gunzip epg_ripper_CA1.xml.gz
        
