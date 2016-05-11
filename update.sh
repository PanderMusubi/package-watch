# remove previous downloads and log
rm -f Sources* urls.log

# download from Debian
dis=debian
for rel in testing jessie
do
    for rep in base updates security backports
    do
        for cat in main non-free contrib
        do
            if [ "$rel" == testing -a "$rep" == backports ]
            then
                continue
            fi
            if [ "$rep" == base ]
            then
                REP=$rel
            else
                REP=$rel-$rep
            fi
            if [ "$rep" = security ]
            then
                url=http://$rep.$dis.org/$dis-$rep/dists/$rel/updates/$cat/source/Sources.gz
            else
                url=http://ftp.$dis.org/$dis/dists/$REP/$cat/source/Sources.gz
            fi
            echo $url >> urls.log
            wget $url
            gunzip Sources.gz
            mv -f Sources Sources-$dis\_$rel\_$rep\_$cat
        done
    done
done

# download from Raspbian
dis=raspbian
for rel in testing jessie
do
    for rep in base
    do
        for cat in main contrib non-free rpi
        do
            if [ "$rel" == testing -a "$rep" == backports ]
            then
                continue
            fi
            if [ "$rep" == base ]
            then
                REP=$rel
            else
                REP=$rel-$rep
            fi
            url=http://archive.$dis.org/$dis/dists/$REP/$cat/source/Sources.gz
            echo $url >> urls.log
            wget $url
            gunzip Sources.gz
            mv -f Sources Sources-$dis\_$rel\_$rep\_$cat
        done
    done
done
dis=raspberrypi
for rel in jessie
do
    for rep in base
    do
        for cat in main ui staging
        do
            if [ "$rel" == testing -a "$rep" == backports ]
            then
                continue
            fi
            if [ "$rep" == base ]
            then
                REP=$rel
            else
                REP=$rel-$rep
            fi
            url=http://archive.$dis.org/debian/dists/$REP/$cat/source/Sources.gz
            echo $url >> urls.log
            wget $url
            gunzip Sources.gz
            mv -f Sources Sources-$dis\_$rel\_$rep\_$cat
        done
    done
done

# download from Ubuntu
dis=ubuntu
for rel in devel xenial
do
    for rep in base updates security backports
    do
        for cat in main restricted universe multiverse
        do
            if [ "$rep" == base ]
            then
                REP=$rel
            else
                REP=$rel-$rep
            fi
            url=http://archive.$dis.com/$dis/dists/$REP/$cat/source/Sources.gz
            echo $url >> urls.log
            wget $url
            gunzip Sources.gz
            mv -f Sources Sources-$dis\_$rel\_$rep\_$cat
        done
    done
done

# process all downloads
./retrieve.py
