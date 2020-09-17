export const initialState = {
    user: 0,
    stockPrice: 0,
};


const reducer = (state, action) => {
    switch(action.type) {

        case 'SET_USER':
            return {
                ...state,
                user: action.user
            }
        case 'SET_PRICE':
            return {
                ...state,
                stockPrice: action.stockPrice
            }
        default:
            return state;
    }
}

export default reducer;