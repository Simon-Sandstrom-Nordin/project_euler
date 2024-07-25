# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    # find min of list (take first if multiple indices are the same)
    max_profit = 0
    min = Float::INFINITY

    price_before = prices[prices.length]
    # remove useless tails
    prices.reverse_each do |price|
        if price <= price_before
            prices.delete_at(0)
        end
        price_before = price_before - 1
    end


    prices.each_with_index do |price_of_buy, ind_of_buy|
        prices.each_with_index do |price_of_sell, ind_of_sell|
            if ind_of_buy <= ind_of_sell
                next
            end

            if price_of_buy - price_of_sell > max_profit
                max_profit = price_of_buy - price_of_sell
            end
        end
    end

    return max_profit
end

puts max_profit([7,1,2,3,4,5,6,0])
