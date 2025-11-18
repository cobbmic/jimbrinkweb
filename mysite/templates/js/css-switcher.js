<script type='text/javascript'>
  function bindEvents(){
  
    var css=document.getElementById('style');
    var col=document.querySelectorAll('a.changeStyle');
    
    /* iterate through collection and assign listener */
    for( var n in col )if( col[n].nodeType==1 ) col[n].onclick=function(e){
      e.preventDefault();/* prevent jumping to top of page etc */
      var el=typeof(e.target)!='undefined' ? e.target : e.srcElement;
      
      /* assign style attributes */
      css.href=el.dataset.style;
      css.rel=el.dataset.rel;
      css.type=el.dataset.type;
      
      /* store reference to style selected in localstorage */
      localStorage.setItem( 'style', el.dataset.style );
  };
  
  /* if there is a reference to the user's css choice in storage, assign it */
  if( localStorage.getItem( 'style' )!=null ) css.href=localStorage.getItem( 'style' );
}

document.addEventListener( 'DOMContentLoaded', bindEvents, false );
</script>
