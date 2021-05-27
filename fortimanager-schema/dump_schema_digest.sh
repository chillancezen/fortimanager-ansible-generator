for schema_file in `ls schemas/`
do
    echo $schema_file
    ././api_schema_parser.py schemas/$schema_file
done
