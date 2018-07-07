using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class Industry : MonoBehaviour {
	public Slider mercury;
	public Slider oil;
	public Slider calcium;
	public Canvas can1;
	//public Canvas can2;
	public Text m1;
	public Text m2;
	public Text m3;
	float Mercury=10,Calcium=10,Oil=10;
	// Use this for initialization
	void Start()
	{
	
		can1.gameObject.SetActive (false);
		//can2.gameObject.SetActive (false);
		mercury.value=0.1f;
		calcium.value = 0.1f;
		oil.value = 0.1f;
	}
	void Update() {
		Mercury = mercury.value*100;
		Calcium = calcium.value*100;
		Oil = oil.value*100;
		m1.text = "Mercury \t\t"+ Mercury.ToString();
		m2.text = "Calcium\t\t"+ Calcium.ToString();
		m3.text = "Oil\t\t" +Oil.ToString();
	}
	void OnTriggerEnter(Collider col)
	{
		if (col.gameObject.tag == "Boat") {
			print ("rgfdg");
			can1.gameObject.SetActive (true);

		}

	}
	void OnTriggerExit(Collider col)
	{
		can1.gameObject.SetActive (false);
		//can2.gameObject.SetActive (false);

	}
}

