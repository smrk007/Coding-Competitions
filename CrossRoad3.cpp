#include <fstream>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

int main(){
    
    // Primary input
    ifstream fin("circlecross.in");
    ofstream fout("circlecross.out");
    
    // For Debugging
    ///ifstream fin("/Users/alexander/Desktop/Coding/USACO/IO Data/input.in");
    ///ofstream fout("/Users/alexander/Desktop/Coding/USACO/IO Data/output.out");
    
    // Initialization of Data
    
    int N;
    fin >> N;
    cout << N; // This makes the program work but I dont know why...?
    
    map<int, vector<int> > cow_data; // cow_data[x][y] -> relation of the xth to the yth cow.
    
    int is_open[N];
    for (int i = 0; i < N; i++){
        is_open[i] = 0;
    }
    
    
    // Principal Code
    
    int pairs = 0;
    
    for (int i = 0; i < 2*N; i++){
        
        int value;
        fin >> value;
        cout << value; // This makes the program work but I don't know why...?
        
        int& openness = is_open[value];
        
        if (openness == 0){ // if closed
            
            openness = 1; // Adjust 'is_open'
            for (int i = 0; i < N; i++){ // Find pairs... Want to make an iterator for this also...
                if (is_open[i] == 1){
                    cow_data[i].push_back(value); // Costly operation..?
                }
            }
            
            
        }else{ // if open
            
            openness = 0; // Adjust 'is_open'
            vector<int>& specific_cow = cow_data[value];
            size_t length = specific_cow.size();
            for (size_t i = 0; i < length; i++){
                if (is_open[specific_cow[i]] == 1){
                    pairs++;
                }
            }
            
            
        }
        
    }
    fout << pairs << endl;
    return 0;
}
