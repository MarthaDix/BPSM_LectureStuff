cat nem.fasta | awk '{
# Is this line a fasta header (the first character is a ">")
if (substr($1,1,1)==">")
 {
print "this is a header line: " $0;
hline=FNR ;
 }
# Identifiy the first line of the seq
if (FNR==hline+1)
 {
print "First line is:" $0;
first_seq_character=substr($0,1,1)
print "First character is: " first_seq_character
print first_seq_character > "first_seq_character.txt"
 }
}'
