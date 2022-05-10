/*
 *  链接：https://www.nowcoder.com/questionTerminal/9fbb4d95e6164cd9ab52e859fbe8f4ec?commentTags=Python
 *  牛牛有N个字符串，他想将这些字符串分类，他认为两个字符串A和B属于同一类需要满足以下条件：
 *  A中交换任意位置的两个字符，最终可以得到B，交换的次数不限。比如：abc与bca就是同一类字符串。
 *  现在牛牛想知道这N个字符串可以分成几类。
 *  
 *  输出一个整数表示分类的个数
 *  4
 *  abcd
 *  abac
 *  aabc
 *  bacd
 *  2 
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


int main()
{
    int n;
    std::string word;
    std::vector<std::string> words;

    std::cin >> n;

    for (int i = 0; i <= n; i++) {
        std::cout << i << std::endl;
        std::getline(std::cin, word);
        if (word != "") 
            words.push_back(word);
    }

    // sort word
    for (auto &word : words) {
        std::sort(word.begin(), word.end());
    }

    // sort words
    std::sort(words.begin(), words.end());

    words.erase(std::unique(words.begin(), words.end()), words.end());

    std::cout << words.size() << std::endl;

    return 0;
}