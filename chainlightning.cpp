#include <bits/stdc++.h>
// #include <boost/algorithm/string.hpp> 

using namespace std;

void split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        if(item=="Ltd" || item=="&" || item == "-" || item=="Trust")
        {    continue;   }
        else{
            elems.push_back(item);
        }
        
    }
}


vector<string> split(const string &s, char delim) {
    vector<string> elems;
    split(s, delim, elems);
    return elems;
}

// vector<string> words;
// words = split(temp,' ');


int main(int argc, char const *argv[])
{
    /*code*/
    string s[500], domain[500];
    int count = 0, line = 0;

    while(getline(cin, s[line])){
        line++; count++;
    }

    //cout<<"lines: "<<line<<" Count : "<<count<<"\n";
    for(int i=0; i<line; i++){
        // cout<<s[i]<<"\n";
        //split();
        vector<string> words;
        words = split(s[i],' ');
        
        domain[i] = "";
        for(int j = 0; j<words.size(); j++){
            //words[j][0] = words[j][0] - 'A' + 'a';
            domain[i]+= words[j]; //to_lower(words[j]);
        }
    }

    for(int i=0; i<line; i++){
        cout<<"www."<<domain[i]<<".co.uk\n";
    }
    return 0;
}
