using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using RestSharp;

namespace AddFeatures
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string layerUrl = "https://services9.arcgis.com/7e6lF03RcLhwFtm5/ArcGIS/rest/services/survey123_d4b3ab2513384ea48ae3cb62a9e0e5df_form/FeatureServer/0";

            Console.WriteLine("Determine url to add features");
            //Determine URL
            string addFeatureUrl = $"{layerUrl}/AddFeatures";

            Console.WriteLine("Creating features string");
            //create json string from feature (from serialization)
            string features = "[{'attributes':{'name':'Maarten','color':'Black','comment':'This is nice :)'},'geometry':{'x':6.1,'y':52.5,'spatialReference':{'wkid':4326}}}]";


            //add feature using RestSharp
            Console.WriteLine("Creating request");
            RestClient rc = new RestClient();
            rc.AcceptedContentTypes = new[] { "application/json" };
            RestRequest request = new RestRequest(addFeatureUrl,Method.Post);
            request.AddParameter("f", "json");
            request.AddParameter("features", features);


            Console.WriteLine("Executing request");
            RestResponse result = rc.Execute(request);

            //write the results
            Console.WriteLine("Getting response content");
            string responsecontent = result.Content;
            Console.WriteLine(responsecontent);

        }
    }
}
