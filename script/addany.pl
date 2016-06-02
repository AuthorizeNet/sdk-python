#author krgupta
#!/usr/local/bin/perl5.8.0

$inp_file = "AnetApiSchema.xsd";
$inp_cmd = "dos2unix $inp_file\n";
#system($inp_cmd);

open(INP,"<$inp_file") or die "Cannot open $inp_file for reading:$!\n";

open(OUP,">AnetOut.xsd") or die "Cannot open AnetOut.xsd for writing\n";
$appd_line = "\<xs:any minOccurs=\"0\" maxOccurs=\"unbounded\" processContents=\"lax\" namespace=\"##any\" \/\>\n";
#print STDOUT "line: $appd_line";

while(<INP>){
        $line=$_;
		if($line =~ /(\t+|\s+)(\<\/xs:sequence)(.*)/){
			$new_line = $1 . "\t" . $appd_line . $line;
			print OUP "$new_line";			
		}
		else{
			print OUP "$line";
		}
}		

