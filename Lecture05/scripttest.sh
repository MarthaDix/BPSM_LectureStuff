#!/bin/bash

input="example_people_data.tsv"
unset count
month=10

rm *.tsvout


tail -n +2 $input | while read name email city birthday_day birthday_month birthday_year country
do
	if  test -z ${name}
	  then
	  echo "Skipping"
	  #count=$((count+1))
	  else
	    count=$((count+1))
	    echo -e "${count} \t ${name} \t ${city} \t ${country}"
	    echo -e "${name} \t ${email} \t ${city} \t ${birthday_day} \t ${birthday_month} \t ${birthday_year}" >> ${country}.tsvout
	    if test ${birthday_month} -eq $month
                then
                echo -e "${count} \t ${name}  \t ${birthday_month} \t ${country}" >> Octbirthday.tsvout
	    else
                continue
	    fi
	fi	
done 
echo "$count"
wc -l Octbirthday.tsvout
head Octbirthday.tsvout
cut -f4 Octbirthday.tsvout | sort | uniq -c | sort -k1,1nr | head -5
