class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float("INF")]*n
        prices[src]= 0

        for i in range(k+1):
            tempPrices = prices.copy()

            for s,d,w in flights:
                if prices[s] == float("INF"):
                    continue
                if prices[s]+w<tempPrices[d]:
                    tempPrices[d] = prices[s]+w

            prices = tempPrices

        return prices[dst] if prices[dst] != float("INF") else -1         
