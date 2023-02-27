
// setting the function to display the properties in a form so each trade can be accepted.
function TradingPost(props) {
    return (
      <table className="table table-hover">
      <div className="post">
        <p> Title: {props.title} </p>
        <p>Username: {props.username}</p>
         <p> Info: {props.text} </p>
        <form action="/trade_accepted" method='POST'>
        <p> Trading: {props.owned_card}</p>
        <input name="owned_card" type="hidden" value={props.owned_card}/>
        <p> Looking for: {props.trade_card}</p>
        <input name="trade_card" type="hidden" value={props.trade_card}/>
        <div class="pt-1 mb-4">
              <button class="btn btn-info btn-lg btn-block" type="submit">Accept</button>
        </div>
       </form>
      </div>
      </table>
    );
  }
  // adding a state object
  function TradingPostContainer() {
    const [posts, setPosts] = React.useState([]);
  
// fetch request used to pull user created posts
  React.useEffect(() => {
    fetch("/all_posts")
      .then((response) => { 
        return response.json()})
      .then((data) => {
        setPosts(data);
    });
  }, []);

  const tradingPosts = [];

// loop through each post and push them to tradingPosts when their properties are set.
  for (const currentPost of posts) {
    console.log(currentPost)
    tradingPosts.push(
      <TradingPost
        key={currentPost.post_Id}
        title={currentPost.post_title}
        username={currentPost.username}
        text={currentPost.post_text}
        owned_card={currentPost.owned_card}
        trade_card={currentPost.trade_card}
      />,
    );
  }
//return and render each post object in tradingPosts in a column at the designated div "container"
  return (
    <React.Fragment>
      <h2>Trading Posts</h2>
      <div className="column">{tradingPosts}</div>
    </React.Fragment>
  );
  }

ReactDOM.render(<TradingPostContainer />, document.querySelector('#container'));