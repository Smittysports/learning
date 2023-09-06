/** Concepts
 * 
 */

/** Views
 * 
 * Views are cheap. They do not perform a copy of the data.
 * 
 * Views also cache! Because of these be very careful if modifying a view and then
 * reading the values... since the values read may be cached and not the newly
 * updated one.
 * 
 * Copying a view works with cached values because it is no longer cached once copied.
 * - If you use a view and modify the underyling data, do not use that view again
 * 
 * Constant propagation
 * - This is broken. You must understant it
 */

#include <iostream>
#include <ranges>

/** Using C++ Concepts
 * This print function is still a template, it simply uses the new easier syntax to remove
 * the need for usin 'template <typename CollT>'
 *
 * Note: There is now no longer a CollT that can be used throughout, like done with classes.
 * That functionality would still require regular tempalte syntax
 * 
 * The auto&& is called 'Universal (or forwarding) reference. It can refer to every expression,
 * event temporaries, withou making it const. This is very useful when using objects that will
 * cache to improve performance (such as a list since it is slow on the first usage of iterators
 * and then is constant time). See the YouTube video by Nicolai Jossutis called C++ Standard Views.
 * 
 * \param coll Takes only a range as an input
 */
void rangedPrint(std::ranges::view auto&& coll)
{
    for (const auto& elem : coll) {
        std::cout << elem << ' ';
    }
    std::cout << '\n';
}