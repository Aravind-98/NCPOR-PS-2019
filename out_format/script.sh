for file in ./in_data/*.nc; do
	python3 convert_to_out.py $file ./out_data/$file
done	
