//This macro runs down the ROI manager and writes lineplots in the current image channel to a specified CSV filepath. Use only with Composite Settings enabled.
function getTitleStripExtension() {
  t = getTitle();
  t = replace(t, ".tif", "");
  t = replace(t, ".dv", "");
  t = replace(t, ".tiff", "");
  t = replace(t, ".lif", "");
  t = replace(t, ".lsm", "");
  t = replace(t, ".czi", "");
  t = replace(t, ".nd2", "");
  return t;
}

shorttitle = ""+getTitleStripExtension()
roinumber = roiManager("Count")

Stack.setPosition(1, 1, 1)

for(j=0; j<roinumber; j++) {
	run("Clear Results");
	roiManager("Select", j);
	profile = getProfile();
  	for (i=0; i<profile.length; i++)
		setResult("Value", i, profile[i]);
	updateResults;
	path = "G:/old_drive/Kia_Wee_Work/Jip4/Lineplots/RPE_Phafin1_2_JIP3_rawlineplots/Phafin1/Ch1/"+shorttitle+"_Ch1_profile_"+j+".csv";
	saveAs("Results", path);
}

Stack.setPosition(2, 1, 1)

for(k=0; k<roinumber; k++) {
	run("Clear Results");
	roiManager("Select", k);
	profile = getProfile();
  	for (i=0; i<profile.length; i++)
		setResult("Value", i, profile[i]);
	updateResults;
	path = "G:/old_drive/Kia_Wee_Work/Jip4/Lineplots/RPE_Phafin1_2_JIP3_rawlineplots/Phafin1/Ch2/"+shorttitle+"_Ch2_profile_"+k+".csv";
	saveAs("Results", path);
}