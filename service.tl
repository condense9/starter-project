
import(frequencies, python_bits, 1);


fn main(word_soup) {
  freqs = async frequencies(word_soup);
  print("Hello from teal!");
  await freqs
}
