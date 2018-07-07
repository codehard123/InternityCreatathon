using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class click : MonoBehaviour {
	public Button bt;
	// Use this for initialization
	void Start () {
		Time.timeScale = 0f;
	}
	
	// Update is called once per frame
	public void Hide () {
		Time.timeScale = 1f;
		bt.gameObject.SetActive (false);
	}
}
