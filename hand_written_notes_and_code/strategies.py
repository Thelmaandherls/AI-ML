from sklearn.tree import DecisionTreeRegressor
from backtesting import Backtest, Strategy

class AnchoredRegression(Strategy):
    limit_buy = 1
    limit_sell = -5
    n_train = 600
    coef_retrain = 200 

    def init(self):
        self.model = DecisionTreeRegressor(max_depth=15, random_state=42)
        self.already_bought = False

        #train model on 1st 600 days 
        X_train = self.data.df.iloc[:self.n_train, :-1] #everything but the last col
        y_train = self.data.df.iloc[:self.n_train, -1] #only the last col - chnage_tomorrow

        self.model.fit(X=X_train, y=y_train)

    def next(self):
        explanatory_today = self.data.df.iloc[[-1], :-1] #take everythigng but last col
        forecast_tomorrow = self.model.predict(explanatory_today)[0] 

        #improve stratgy to get higher equity via changign the numbers here or using the bt optimisation method
        if forecast_tomorrow > self.limit_buy and self.already_bought == False: 
            self.buy() 
            self.already_bought = True 
        elif forecast_tomorrow < self.limit_sell and self.already_bought== True: 
            self.sell() 
            self.already_bought = False
        else: 
            pass

#intialise the mdoel by first training it on the first 600 days 
            
# To take action on whether to buy/sell a stock req a new class that 
# Contains the anchored walk forward procedure 
# Once model has been intialised, starts the walk forward backtest 
# According to these conditions 

class WalkForwardAnchored(AnchoredRegression):
    def next(self):
        # Take no action and ove onto following day until thr data have been 
        # Trained for at least 600 days 
        if len(self.data) < self.n_train:
            return 
        
        # Retrain the model every 200 days after intial 600 day trianinig
        if len(self.data) % self.coef_retrain == 0:
            X_train = self.data.df.iloc[:, :-1]
            y_train = self.data.df.iloc[:, -1]

            self.model.fit(X_train, y_train)

            # Taking the next function from the inherited Regression clads
            super().next()
        
        else:
            super().next()

class WalkForwardUnAnchored(AnchoredRegression):
    #only thing that chnages is how x and y train are slected 

    def next(self):
        # Take no action and ove onto following day until thr data have been 
        # Trained for at least 600 days 
        if len(self.data) < self.n_train:
            return 
        
        # Retrain the model every 200 days after intial 600 day trianinig
        if len(self.data) % self.coef_retrain == 0:
            X_train = self.data.df.iloc[-self.n_train:, :-1]
            y_train = self.data.df.iloc[-self.n_train:, -1]

            self.model.fit(X_train, y_train)

            # Taking the next function from the inherited Regression clads
            super().next()
        
        else:
            super().next()