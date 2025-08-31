function extract_ultrasonic_data(filename)
m=dlmread(filename,',',0,0);
Time=m(:,1);
A=m(:,2);


newName = strrep(filename,'csv','mat');
newName
save(newName,'A')