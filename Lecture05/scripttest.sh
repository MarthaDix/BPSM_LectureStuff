#!/bin/bash

input="example_people_data.tsv"
unset count

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
	fi	
done 
echo "$count"
