# This code was copied from https://avro.apache.org/docs/1.8.2/gettingstartedpython.html
# and modified for my use case of printing the contents of an avro file.
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("test.avsc", "rb").read())

#writer = DataFileWriter(open("test.avro", "wb"), DatumWriter(), schema)
#writer.append({"name": "Alyssa", "favorite_number": 256})
#writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
#writer.close()

reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print user
reader.close()
