#!/bin/bash 

construct_input () {
	work_dir=${1}
    input_file=${2}
    unzip_dir="${1}/$(basename ${input_file} .zip)"
	mkdir -p ${unzip_dir}
	unzip ${input_file} -d ${unzip_dir}
}

destruct_input() {
	input_file=$2
    unzip_dir="${1}/$(basename ${input_file} .zip)"
    rm -rf ${unzip_dir}
}

main(){
	wrk_dir=$1 
	output_file=$2 
	shift 
	shift 

	# Generate the Header of the Data file 
	echo "Notebook ForLoops RangeIters MaxDepth" > ${output_file}
	for file in $@; do 
    	unzip_dir="${wrk_dir}/$(basename ${file} .zip)"
		construct_input  ${wrk_dir} ${file}
		for ipfile in $(ls ${unzip_dir}); do
			python3 $(pwd)/parser.py ${unzip_dir}/${ipfile} >> ${output_file}
		done 
		destruct_input  ${wrk_dir} ${file}
	done 
    awk '$2 != "failure" { printf("%s\n",$0); }' ${output_file} >> $(dirname ${output_file})/filt_$(basename ${output_file})
	# change space separated to csv
	sed -i -e 's/ /,/g' $(dirname ${output_file})/filt_$(basename ${output_file})
}

main $(pwd)/data/download $(pwd)/total.csv $(pwd)/data/download/download_*.zip 
