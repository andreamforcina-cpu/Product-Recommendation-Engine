from product_data import products

# Step 1 - Print out the products to see the data that you are working with.
print(products)


# Step 2 - Create a list called customer_preferences
# and store the user preferences in this list.
customer_preferences = []

response = ""

while response != "N":
    print("Input a preference:")
    preference = input().lower()

    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()


# Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)


# Step 4 - Convert the product tags to sets
# in order to allow for faster comparisons.
converted_products = []

for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }

    converted_products.append(converted_product)


# Step 5 - Calculate the number of matching tags.
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''

    matches = product_tags.intersection(customer_tags)
    return len(matches)


# Step 6 - Loop over all products and return a sorted list of matches.
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''

    recommendations = []

    for product in products:
        match_count = count_matches(product["tags"], customer_tags)

        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "matches": match_count
            })

    recommendations.sort(
        key=lambda product: product["matches"],
        reverse=True
    )

    return recommendations


# Step 7 - Call the function and print the results.
recommended_products = recommend_products(
    converted_products,
    customer_preferences
)

print("\nRecommended Products:")

for product in recommended_products:
    print(
        "- " + product["name"] +
        " (" + str(product["matches"]) + " match(es))"
    )


# DESIGN MEMO
#
# For this product recommendation program, I used lists, sets, loops,
# functions, and set intersections. I first used a list to collect the
# customer's preferences because lists make it easy to add new values
# with append(). After the customer finishes entering preferences, I
# convert the list into a set. This removes duplicate preferences
# automatically. For example, if a customer enters "durable" twice,
# the set will only keep it once.
#
# I also converted each product's tags into a set. Sets are useful for
# this program because they make it easier and faster to compare the
# customer's preferences with the tags of each product. I used the
# intersection() operation to find values that exist in both sets.
# The count_matches() function counts these matching tags and returns
# the total number of matches.
#
# The recommend_products() function uses a loop to check every product.
# If a product has at least one matching tag, its name and match count
# are added to a recommendation list. The list is then sorted so the
# products with the most matches appear first.
#
# If the catalog had more than 1,000 products, I would want to make the
# program more efficient. Sets already make comparisons faster, but a
# larger system could organize products by tags instead of checking
# every product individually. A real recommendation system could also
# use a database to store products and customer preferences.