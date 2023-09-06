#include <iostream>

/** Prior to C++ 20
 * Typical template usage
 */
template <typename CollT>
void print(const CollT& coll)
{
    for (const auto& elem : coll) {
        std::cout << elem << ' ';
    }
    std::cout << '\n';
}
/** C++20 This print function is still a template, it simply uses the new easier syntax to remove
 * the need for usin 'template <typename CollT>'
 *
 * Note: There is now no longer a CollT that can be used throughout, like done with classes.
 * That functionality would still require regular tempalte syntax
 */
void print2(const auto& coll)
{
    for (const auto& elem : coll) {
        std::cout << elem << ' ';
    }
    std::cout << '\n';
}

