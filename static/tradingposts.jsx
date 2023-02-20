


function TradingPost(props) {
    console.log(props)
    return (
      <div className="post">
        <p> Title: {props.title} </p>
        <p>Username: {props.username}</p>
         <p> Info: {props.text} </p>
        <form action="/trade_accepted" method='POST'>
        <p> Trading: {props.owned_card}</p>
        <input name="owned_card" type="hidden" value={props.owned_card}/>
        <p> Looking for: {props.trade_card}</p>
        <input name="trade_card" type="hidden" value={props.trade_card}/>
        <input type="submit" value="Accept Trade?"/>
       </form>
      </div>
    );
  }
  function TradingPostContainer() {
    const [posts, setPosts] = React.useState([]);
  

  React.useEffect(() => {
    fetch("/all_posts")
      .then((response) => { 
        return response.json()})
      .then((data) => {
        setPosts(data);
    });
  }, []);

  const tradingPosts = [];


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

  return (
    <React.Fragment>
      <h2>Trading Posts</h2>
      <div className="column">{tradingPosts}</div>
    </React.Fragment>
  );
  }

ReactDOM.render(<TradingPostContainer />, document.querySelector('#container'));