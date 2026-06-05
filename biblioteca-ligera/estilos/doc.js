/* doc.js · Prompt Amplificado · interacción compartida · homólogo a Jarvis OS runbook/playbook */
(function(){
  var html=document.documentElement;
  /* persisted theme + lang */
  try{var t=localStorage.getItem('mdg_theme');if(t==='dark')html.dataset.theme='dark';var l=localStorage.getItem('mdg_locale');if(l==='en'||l==='pt')html.lang=l;}catch(e){}
  var langs=['es','en','pt'];
  function setLang(l){if(langs.indexOf(l)<0)l='es';html.lang=l;try{localStorage.setItem('mdg_locale',l)}catch(e){}var lb=document.getElementById('langbtn');if(lb)lb.textContent=l.toUpperCase();}
  function setTheme(v){html.dataset.theme=v;try{localStorage.setItem('mdg_theme',v)}catch(e){}var tb=document.getElementById('theme');if(tb)tb.textContent=v==='dark'?'☀':'☾';}
  document.addEventListener('DOMContentLoaded',function(){
    setLang(html.lang||'es');
    var tb=document.getElementById('theme'); if(tb){tb.textContent=html.dataset.theme==='dark'?'☀':'☾';tb.onclick=function(){setTheme(html.dataset.theme==='dark'?'light':'dark')};}
    var lb=document.getElementById('langbtn'); if(lb)lb.onclick=function(){var i=langs.indexOf(html.lang);setLang(langs[(i+1)%langs.length]);};
    /* reading progress */
    var rp=document.querySelector('.reading-progress');
    if(rp)window.addEventListener('scroll',function(){var h=document.documentElement;var sc=(h.scrollTop)/((h.scrollHeight-h.clientHeight)||1);rp.style.width=(sc*100)+'%';},{passive:true});
  });

  /* ----- row-modal: click en fila con data-detail o data-modal ----- */
  function openRowModal(title,h){
    var m=document.getElementById('row-modal');if(!m)return;
    var t=m.querySelector('#row-modal-title');if(t)t.innerHTML=title||'Detalle';
    var b=m.querySelector('#row-modal-body');if(b)b.innerHTML=h||'';
    if(m.showModal)m.showModal();else m.setAttribute('open','');
  }
  document.addEventListener('click',function(e){
    /* close buttons / backdrop */
    if(e.target.matches('[data-close]')){var dlg=e.target.closest('dialog');if(dlg)dlg.close();return;}
    var dial=e.target.closest('dialog.smodal');
    if(dial&&e.target===dial){dial.close();return;}
    if(e.target.closest('a,button,input,label,.codebox,.prompt-copyable'))return;
    var tr=e.target.closest('tr');if(!tr)return;
    var mid=tr.getAttribute('data-modal');
    if(mid){var d=document.getElementById(mid);if(d){if(d.showModal)d.showModal();else d.setAttribute('open','');}return;}
    var det=tr.getAttribute('data-detail');
    if(det){openRowModal(tr.getAttribute('data-title')||'Detalle',det);}
  });

  /* ----- prompts copiables ----- */
  function visiblePre(box){
    var lang=document.documentElement.lang||'es';
    return box.querySelector('.prompt-text.l-'+lang+',pre.l-'+lang)||box.querySelector('.prompt-text,pre');
  }
  window.copyPrompt=function(btn){
    var box=btn.closest('.prompt-copyable')||btn.closest('.codebox');if(!box)return;
    var pre=visiblePre(box);if(!pre)return;
    var tx=pre.textContent.trim();
    function flash(){var done={es:'Copiado ✓',en:'Copied ✓',pt:'Copiado ✓'}[document.documentElement.lang]||'Copiado ✓';var old=btn.textContent;btn.textContent=done;btn.classList.add('ok');setTimeout(function(){btn.textContent=old;btn.classList.remove('ok')},1600);}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(tx).then(flash).catch(fb);}else{fb();}
    function fb(){var ta=document.createElement('textarea');ta.value=tx;ta.style.position='absolute';ta.style.left='-9999px';document.body.appendChild(ta);ta.select();try{document.execCommand('copy')}catch(e){}document.body.removeChild(ta);flash();}
  };
  window.downloadPrompt=function(btn,filename){
    var box=btn.closest('.prompt-copyable')||btn.closest('.codebox');if(!box)return;
    var pre=visiblePre(box);if(!pre)return;
    var blob=new Blob([pre.textContent.trim()],{type:'text/markdown'});
    var u=URL.createObjectURL(blob);var a=document.createElement('a');a.href=u;a.download=filename||'prompt.md';a.click();URL.revokeObjectURL(u);
  };
})();
