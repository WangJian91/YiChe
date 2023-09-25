dir=$1
file=$2
out_file=$3

python get_numers.py $dir/$file > $dir/$out_file


xt_break_count=$(cat $dir/$out_file | awk -F '\t' '$5!="用户挂断"{print $1}' | sort | uniq | wc -l)
yh_break_count=$(cat $dir/$out_file | awk -F '\t' '$5=="用户挂断"{print $1}' | sort | uniq | wc -l)
echo "系统挂断数:"$xt_break_count
echo "用户挂断数:"$yh_break_count

yh_break_asrfalse=$(cat $dir/$out_file | awk -F '\t' '$5=="用户挂断"&&$6=="ASR错误"{print $1}'| sort | uniq | wc -l)
echo "用户挂断ASR错误数:"$yh_break_asrfalse
xt_break_asrfalse=$(cat $dir/$out_file | awk -F '\t' '$5!="用户挂断"&&$6=="ASR错误"{print $1}'| sort | uniq | wc -l)
echo "系统挂断ASR错误:"$xt_break_asrfalse
yh_break_nlufalse=$(cat $dir/$out_file | awk -F '\t' '$5=="用户挂断"&&$7=="0"{print $1}' | sort | uniq | wc -l)
echo "用户挂断NLU错误数:"$yh_break_nlufalse
xt_break_nlufalse=$(cat $dir/$out_file | awk -F '\t' '$5!="用户挂断"&&$7=="0"{print $1}' | sort | uniq | wc -l)
echo "系统挂断NLU错误:"$xt_break_nlufalse
yh_break_breakfalse=$(cat $dir/$out_file | awk -F '\t' '$5=="用户挂断"&&$8!="用户未被打断"{print $1}' | sort | uniq | wc -l)
echo "用户挂断:用户被打断数:"$yh_break_breakfalse
xt_break_breakfalse=$(cat $dir/$out_file | awk -F '\t' '$5!="用户挂断"&&$8!="用户未被打断"{print $1}' | sort | uniq | wc -l)
echo "系统挂断:用户被打断数:"$xt_break_breakfalse
yh_break_noisefalse=$(cat $dir/$out_file | awk -F '\t' '$5=="用户挂断"&&$9=="存在噪音"{print $1}'| sort | uniq | wc -l)
echo "用户挂断:存在噪音数:"$yh_break_noisefalse
xt_break_noisefalse=$(cat $dir/$out_file | awk -F '\t' '$5!="用户挂断"&&$9=="存在噪音"{print $1}'| sort | uniq | wc -l)
echo "系统挂断:存在噪音数:"$xt_break_noisefalse

echo "===================="

echo "用户挂断ASR错误占比:0"`echo "scale=2; $yh_break_asrfalse / $yh_break_count" | bc`
echo "系统挂断ASR错误占比:0"`echo "scale=2; $xt_break_asrfalse / $xt_break_count" | bc`
echo "用户挂断NLU错误占比:0"`echo "scale=2; $yh_break_nlufalse / $yh_break_count" | bc`
echo "系统挂断NLU错误占比:0"`echo "scale=2; $xt_break_nlufalse / $xt_break_count" | bc`
echo "用户挂断:用户被打断占比:0"`echo "scale=2; $yh_break_breakfalse / $yh_break_count" | bc`
echo "系统挂断:用户被打断占比:0"`echo "scale=2; $xt_break_breakfalse / $xt_break_count" | bc`
echo "用户挂断:存在噪音占比:0"`echo "scale=2; $yh_break_noisefalse / $yh_break_count" | bc`
echo "系统挂断:存在噪音占比:0"`echo "scale=2; $xt_break_noisefalse / $yh_break_count" | bc`
