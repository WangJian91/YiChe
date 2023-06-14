path=$1
file=$2
output=$3
python wide_tabel.py $path/$file > $path/$output
cat $path/$output  | awk -F '\t' 'NF>=20&&$9!="2"{print $2"\t"$8"\t"$9"\t"$14}' > $path/$output'_pure'
