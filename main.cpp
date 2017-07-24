#include <AquesTalk2.h>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  int size = 0;
  unsigned char *wav_ptr = AquesTalk2_Synthe_Utf8("ハローワールド", 100, &size, 0);

  if (wav_ptr) {
    ofstream wav_file("hello_world.wav", ios::out | ios::binary);
    wav_file.write((char *)wav_ptr, size);
    wav_file.close();

    AquesTalk2_FreeWave(wav_ptr);
  } else {
    cerr << "wav_ptr is null" << endl;
  }

  return 0;
}
